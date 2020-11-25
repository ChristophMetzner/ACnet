import ACnet_NMDAparams
from netpyne import sim
import os,sys
import numpy as np
import shutil
import pickle


def run(name, conn_seeds_file, noise_seeds_file, freq):
    conn_seeds = np.load(conn_seeds_file)
    noise_seeds = np.load(noise_seeds_file)

    #conn_seeds = [123]  # only for test purposes
    #noise_seeds = [123]  # only for test purposes

    frequencies = [float(freq)]
    # run sims for different subjects
    for i, cs in enumerate(conn_seeds):
        # if i>15:
        print(i)
        # different subject
        directory = './Subject_' + str(i)
        print(directory)
        if not os.path.isdir(directory):
            print('Creating directoy:', directory)
            os.mkdir(directory)
        for j, ns in enumerate(noise_seeds):
            # different trials for each subject
            for f in frequencies:
                ACnet_NMDAparams.simConfig.filename = directory + '/ACnet_NMDA_'+name+'_trial_' + str(j) + '_' + str(
                    int(f)) + 'Hz'  # Set file output name
                ACnet_NMDAparams.simConfig.seeds = {'conn': cs, 'stim': ns, 'loc': 1}  # Seeds for randomizers
                # (connectivity , input stimulation and cell locations)
                ACnet_NMDAparams.netParams.stimSourceParams['drive'] = {'type': 'NetStim', 'rate': f, 'noise': 0.0,
                                                                        'start': 1000.0}

                sim.createSimulateAnalyze(netParams=ACnet_NMDAparams.netParams, simConfig=ACnet_NMDAparams.simConfig)



def analyze(name,conn_seeds_file,noise_seeds_file,freq):
    conn_seeds = np.load(conn_seeds_file)
    noise_seeds = np.load(noise_seeds_file)

    frequencies = [float(freq)]

    #conn_seeds = [123]  # only for test purposes
    #noise_seeds = [123]  # only for test purposes

    dt = 0.1
    duration = 2000
    timepoints = int((duration / dt) / 2)

    n = len(conn_seeds)
    m = len(noise_seeds)
    lfps = np.zeros((n, m, 1, timepoints))

    print(os.getcwd())

    # Load data
    for i, cs in enumerate(conn_seeds):
        print(i)
        # different subject
        directory = './Subject_' + str(i)
        for j, ns in enumerate(noise_seeds):
            print(j)
            for k, fr in enumerate(frequencies):
                print(fr)
                # different trials for each subject
                filename = directory + '/ACnet_NMDA_'+name+'_trial_' + str(j) + '_' + str(int(fr)) + 'Hz.pkl'
                f = open(filename, 'rb')
                data = pickle.load(f)
                lfp = data['simData']['LFP'][10000:20000]
                lfp = [x[0] for x in lfp]
                lfps[i, j, k, :] = lfp

    savefile1 = name+'-Data.npy'
    savefile2 = '../../LFP-Data/'+name+'-Data.npy'
    np.save(savefile1, lfps)
    np.save(savefile2, lfps)

def cleanup(name):
    # zip data
    os.chdir('/home/cmetzner/ACnet/')
    shutil.make_archive(name, 'zip', name)  # make_archive only works for zip-files < 2GB! (but here files are ~550MB)
    # delete data
    shutil.rmtree(name)


def main():
    args = sys.argv[1:]
    # run sims
    run(args[0],args[1],args[2],args[3])
    # analyze them
    analyze(args[0],args[1],args[2],args[3])
    # zip and delete files
    cleanup(args[0])

if __name__ == '__main__':
    main()
