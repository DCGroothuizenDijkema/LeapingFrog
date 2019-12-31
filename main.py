
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
from num2words import num2words

from huygens.plotting import simulation_plot,setup_simulation_plot
from frog import simulate,probability,harmonic,simulate_py

output_dir='./out/' # change if you want the plots somewhere else
try:
  os.makedirs(output_dir) 
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
  '''
  '''
  # constants
  num_pads=10
  num_itr=1000000
  num_runs=150
  run_size=10

  assert num_runs%run_size==0, "`num_runs` is not a multiple of `run_size`"

  plot_name='LeapingFrog.png'
  image_res=1200

  # control
  save_fig=True
  show_fig=False
  verbose=True

  # get figure and axis to plot on
  ordinal=num2words(num_pads, to='ordinal').capitalize()
  _,ax=setup_simulation_plot(x_lim=(1,num_itr),title='Approximating the {} Harmonic Number'.format(ordinal),x_label='Iteration',
    y_label=r'Estimate of $H_{%d}$'%num_pads)

  # perform the simulation
  last_run=int(num_runs/run_size)-1
  data=np.empty((run_size,num_itr))
  for run in range(int(num_runs/run_size)):
    for sim in range(run_size):
      if verbose:
        print('Run: {}; Sim: {}'.format(run,sim))
      data[sim,:]=simulate(10,num_itr)
    # if it's the last run, plot the actual value along with the data
    # otherwise, just plot the data
    if run==last_run:
      ax=simulation_plot(data,np.arange(num_itr),ax=ax,hline=harmonic(10),hline_linewidth=1.5,hline_alpha=0.9)
    else:
      ax=simulation_plot(data,np.arange(num_itr),ax=ax)

  # output
  if save_fig:
    plt.savefig('{}{}'.format(output_dir,plot_name),dpi=image_res,bbox_inches='tight',pad_inches=0.25)
  if show_fig:
    plt.show()

def time_comparison():
  '''
  '''
  # constants
  num_pads=10
  num_itr=100000

  # time the compiled C++
  t0_cpp=time()
  simulate(num_pads,num_itr)
  t1_cpp=time()

  # time Python
  t0_py=time()
  simulate_py(num_pads,num_itr)
  t1_py=time()

  # output
  print('Python duration: {}s'.format(t1_py-t0_py))
  print('Compiled C++ duration: {}s'.format(t1_cpp-t0_cpp))


if __name__=='__main__':
  run()
  # time_comparison()