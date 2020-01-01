
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# main.py                                                                                                                               //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - December, 2019                                                                                            //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

# Main file to execute the solution to the leaping frog problem

from time import process_time as time
import errno
import os

import matplotlib.pyplot as plt
import numpy as np
from num2words import num2words

from huygens.plotting import simulation_plot,setup_simulation_plot
from frog import simulate,simulate_py,harmonic

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

Running the Simulation
======================
The `run()` function can be used to obtain an answer to the problem and produce a visualisation of the simulation process.

`num_pads` determines the width of the river, including the other bank. `num_itr` determines the number of crossings in one run of the
simulation while `num_runs` is the number of runs of the simulation. `run_size` is needed to minimise the amount of memory required by the
process by splitting the simulations into batches. `num_runs` should be a multiple of `run_size`.

`plot_name` gives the name of the file the plot is save to, and should include the file format. The plot is saved to the folder specified in
`output_dir`, set at the top of this file. `image_res` gives the dots per inch of the plot

If the visualisation needs to be saved, set `save_fig` to `True`; if it simply needs to be displayed, set `show_fig` to `True`. To see a
counter as the simulations are carried out (useful if the runtime is long, therefore confirming that something is happening), and to
display the approximation of the average, set `verbose` to True.

Comparing Speeds
================
The `time_comparison()` function can be used to compare the speed of Python to that of compiled C++. Both the `num_pads` and `num_itr`
options can be set. The former determines the width of the river, including the other bank, while the latter determines the number of
crossings in one run of the simulation. The default values of 10 and 100,000, respectively, provide a good balance between demonstrating
the difference in speeds without taking too long (about 3 seconds in total). These values are also close to those which produced the plot
in the README.

'''

def run():
  '''
  Produce a Monte Carlo approximation, and a plot detailing the process, of a certain harmonic number.

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
  mean=[]
  last_run=int(num_runs/run_size)-1
  data=np.empty((run_size,num_itr))
  for run in range(int(num_runs/run_size)):
    for sim in range(run_size):
      if verbose:
        print('Run: {}; Sim: {}'.format(run,sim))
      data[sim,:]=simulate(10,num_itr)
    # keep track of the means
    mean.append(np.mean(data[:,-1]))
    # if it's the last run, plot the actual value along with the data
    # otherwise, just plot the data
    if run==last_run:
      ax=simulation_plot(data,np.arange(num_itr),ax=ax,hline=harmonic(10),hline_linewidth=1.5,hline_alpha=0.9)
    else:
      ax=simulation_plot(data,np.arange(num_itr),ax=ax)

  # output
  if verbose:
    print('The {} harmonic number is approximately {:.4f}'.format(ordinal.lower(),np.mean(mean)))
  if save_fig:
    plt.savefig('{}{}'.format(output_dir,plot_name),dpi=image_res,bbox_inches='tight',pad_inches=0.25)
  if show_fig:
    plt.show()

def time_comparison():
  '''
  Compare the speeds of compiled C++ and Python code.

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