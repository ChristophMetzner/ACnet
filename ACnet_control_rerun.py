from ACnet_run_40_only import run,analyze,cleanup
import numpy as np
import os
import subprocess as sp





# conn_seeds = [123]
# noise_seeds = [123]

freq = 40.0

conn_seeds_file = 'Conn-Seeds.npy'
noise_seeds_file = 'Noise-Seeds.npy'


name = 'Control_rerun'
# go to folder
os.chdir(name)
call = "python ACnet_run_40_only.py "+name+" "+conn_seeds_file+" "+noise_seeds_file+" "+str(freq)
print call
sp.call([call], shell=True)
os.chdir('/home/cm15acr/Gene-Variants-And-Gamma/Automatic_Variants/')

