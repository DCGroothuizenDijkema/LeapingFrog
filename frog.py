
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
#                                                                                                                                       //
# frog.py                                                                                                                               //
#                                                                                                                                       //
# D. C. Groothuizen Dijkema - December, 2019                                                                                            //
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

# Helper function file for the solution to the leaping frog problem


import ctypes as ct
import numpy as np

from huygens.interf import c_vector

__all__=['simulate','average','harmonic']

# load the lib
_libc=ct.cdll.LoadLibrary('./bin/frog.dll')

# extract the functions
_simulate=getattr(_libc,'?simulate@@YAXHHQEAN@Z')
_average=getattr(_libc,'?average@@YANHH@Z')
_harmonic=getattr(_libc,'?harmonic@@YANI@Z')

# assign arg and return types
_simulate.argtypes=[ct.c_int,ct.c_int,ct.POINTER(ct.c_double)]
_simulate.restype=None
_average.argtypes=[ct.c_int,ct.c_int]
_average.restype=ct.c_double
_harmonic.argtypes=[ct.c_int]
_harmonic.restype=ct.c_double

def simulate(num_pads,num_itr):
  '''
  Simulate numerous processions of a frog leaping across a river to determine the average number of leaps needed.

  Parameters
  ----------
  num_pads : int
    The number of pads, including the other bank, the frog needs to leap.
  num_itr : int
    The number of times the simulation should be run.

  Returns
  -------
  means : numpy.ndarray
    The moving average number of leaps needed to cross the river across the simulations.

  '''
  means=c_vector(ct.c_double,num_itr)
  _simulate(num_pads,num_itr,means)
  
  return np.ctypeslib.as_array(means)

def average(num_pads,num_itr):
  '''
  Determine the average number of leaps needed for a frog to cross a river.

  Parameters
  ----------
  num_pads : int
    The number of pads, including the other bank, the frog needs to leap.
  num_itr : int
    The number of times the simulation should be run.

  Returns
  -------
  mean : float
    The average number of leaps needed to cross the river.

  '''
  return _average(ct.c_int(num_pads),ct.c_int(num_itr))

def harmonic(n):
  '''
  Determine a given harmonic number.

  Parameters
  ----------
  n : int
    A positive integer.

  Returns
  -------
  h : float
    The `n`th harmonic number.

  Raises
  ------
  TypeError
    If n is not a positive integer.

  '''
  try:
    return _harmonic(ct.c_int(n))
  except WindowsError:
    raise TypeError('`n` must be a positive integer.')

def simulate_py(num_pads,num_itr):
  '''
  Determine the average number of leaps needed to reach the other bank, storing the running approximation of the mean.
  
  Parameters
  ----------
  num_pads : int
    The number of pads to the other bank, including the other bank.
  num_itr : int
    The number of times to run the simulation.
    The higher `num_itr` is, the more accurate the approximation.
  
  Returns
  -------
  ma : numpy.ndarray
    The moving average of the number of leaps needed to reach the other bank.

  '''
  ma=np.empty(num_itr)
  mean=0

  for itr in range(num_itr):
    jumps=leap_py(num_pads,0)
    mean+=(jumps-mean)/(itr+1)
    ma[itr]=mean

  return ma

def leap_py(pads_left,leaps_made):
  '''
  Determine, using recursion, the number of leaps needed to reach the other bank.

  Parameters
  ----------
  pads_left : int
    The number of pads left to reach the other bank, including the other bank.
  leaps_made : int
    The number of leaps already made.

  Returns
  -------
  leaps : int
    The number of leaps needed to reach the other bank from the current pad.

  '''
  if pads_left==0: return leaps_made

  leap=np.random.random_integers(1,pads_left)
  return leap_py(pads_left-leap,leaps_made+1)
