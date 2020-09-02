from ACnet_run_40_only import run,analyze,cleanup
import numpy as np
import os
import subprocess as sp





# conn_seeds = [123]
# noise_seeds = [123]

freq = 40.0

conn_seeds_file = 'Conn-Seeds.npy'
noise_seeds_file = 'Noise-Seeds.npy'

names = ['High_noise_irr_ctrl']
for name in names:
    # go to folder
    os.chdir(name)
    call = "python ACnet_run_40_only.py "+name+" "+conn_seeds_file+" "+noise_seeds_file+" "+str(freq)
    print call
    sp.call([call], shell=True)
    os.chdir('/home/cmetzner/Gene-Variants-and-Gamma/Automatic_Variants/')

