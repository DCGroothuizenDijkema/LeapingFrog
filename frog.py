
import ctypes as ct
import numpy as np

from huygens.interf import c_vector

__all__=['simulate','probability','harmonic']

# load the lib
_libc=ct.cdll.LoadLibrary('./bin/frog.dll')

# extract the functions
_simulate=getattr(_libc, '?simulate@@YAXHHQEAN@Z')
_probability=getattr(_libc, '?average@@YANHH@Z')
_harmonic=getattr(_libc,'?harmonic@@YANI@Z')

# assign arg and return types
_simulate.argtypes=[ct.c_int,ct.c_int,ct.POINTER(ct.c_double)]
_simulate.restype=None
_probability.argtypes=[ct.c_int,ct.c_int]
_probability.restype=ct.c_double
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

def probability(num_pads,num_itr):
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
  return _probability(ct.c_int(num_pads),ct.c_int(num_itr))

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
