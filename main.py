
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# main.py                                                                                                                               //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - December, 2019                                                                                            //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

from time import process_time as time
import errno
import os

import matplotlib.pyplot as plt
import numpy as np

from huygens.plotting import simulation_plot,setup_simulation_plot
from frog import simulate,probability,harmonic,simulate_py

out_dir='./out/' # change if you want the plots somewhere else
try:
  os.makedirs(out_dir) 
except OSError as err:
  if err.errno != errno.EEXIST:
    raise

'''
============
Instructions
============

This Python script contains two functions, one for approximating a given harmonic number and one for comparing the speeds of Python and
compiled C++.

'''

def run():
  num_pads=10
  num_itr=1000000
  num_runs=150
  run_size=10

def time_comparison():
  pass

if __name__=='__main__':
  run()
  # time_comparison()