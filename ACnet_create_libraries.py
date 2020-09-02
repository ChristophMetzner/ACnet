import variations
import os,shutil

ca_vars = 76
atp_vars = 1
scn_vars = 6
hcn_vars = 4


variants = variations.VARS
var_list = [6]

#params_file = 'ACnet_NMDAparams_drive_05.py'
#params_file = 'ACnet_NMDAparams_drive_0625.py'
#params_file = 'ACnet_NMDAparams_drive_075.py'
#params_file = 'ACnet_NMDAparams_drive_0875.py'
#params_file = 'ACnet_NMDAparams.py'
params_file = 'ACnet_NMDAparams_high_noise_irr.py'
high_noise = 1
for i in var_list:
    name = 'CA_VAR' + str(i+1)
    fname = name
    if high_noise:
        fname = name + '_high_noise_irr'
    # create folder
    if not os.path.isdir(name):
        print 'Creating base directoy:', name
        os.mkdir(name)
    # copy all files
    shutil.copytree('mod_files', fname+'/mod_files')
    shutil.copytree('Cells', fname+'/Cells')
    shutil.copyfile('variation_utils.py', fname+'/variation_utils.py')
    shutil.copyfile('ACnet_run_40_only.py', fname+'/ACnet_run_40_only.py')
    shutil.copyfile(params_file, fname+'/ACnet_NMDAparams.py')
    shutil.copyfile('Conn-Seeds.npy', fname+'/Conn-Seeds.npy')
    shutil.copyfile('Noise-Seeds.npy', fname+'/Noise-Seeds.npy')
    shutil.copyfile('Inh_CellList.npy', fname+'/Inh_CellList.npy')
    # change directory
    os.chdir(fname)
    print os.getcwd()
    from variation_utils import set_var, compile
    # change mod files and compile
    var = variants[name]
    print var
    set_var(var)
    compile()
    os.chdir('/home/cmetzner/Gene-Variants-and-Gamma/Automatic_Variants/')

