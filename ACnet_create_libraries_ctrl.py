import variations
import os,shutil


names = ['High_noise_irr_ctrl']

#params_file = 'ACnet_NMDAparams_drive_05.py'
#params_file = 'ACnet_NMDAparams_drive_0625.py'
#params_file = 'ACnet_NMDAparams_drive_075.py'
#params_file = 'ACnet_NMDAparams_drive_0875.py'
#params_file = 'ACnet_NMDAparams.py'
params_file = 'ACnet_NMDAparams_high_noise_irr.py'
for name in names:
    # create folder
    if not os.path.isdir(name):
        print 'Creating base directoy:', name
        os.mkdir(name)
    # copy all files
    shutil.copytree('mod_files', name+'/mod_files')
    shutil.copytree('Cells', name+'/Cells')
    shutil.copyfile('variation_utils.py', name+'/variation_utils.py')
    shutil.copyfile('ACnet_run_40_only.py', name+'/ACnet_run_40_only.py')
    shutil.copyfile(params_file, name+'/ACnet_NMDAparams.py')
    shutil.copyfile('Conn-Seeds.npy', name+'/Conn-Seeds.npy')
    shutil.copyfile('Noise-Seeds.npy', name+'/Noise-Seeds.npy')
    shutil.copyfile('Inh_CellList.npy', name+'/Inh_CellList.npy')
    # change directory
    os.chdir(name)
    print os.getcwd()
    from variation_utils import compile
    compile()
    os.chdir('/home/cmetzner/Gene-Variants-and-Gamma/Automatic_Variants/')

