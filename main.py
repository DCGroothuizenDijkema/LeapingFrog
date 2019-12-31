
from time import process_time as time
import errno
import os

import matplotlib.pyplot as plt
import numpy as np

from huygens.plotting import simulation_plot,setup_simulation_plot
from frog import simulate,harmonic

try:
  os.makedirs('./out/')
except OSError as err:
  if err.errno != errno.EEXIST:
    raise

def run():
  pass

def time_comparison():
  pass

if __name__=='__main__':
  run()
  # time_comparison()