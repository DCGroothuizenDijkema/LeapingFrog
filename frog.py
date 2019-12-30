
import ctypes as ct
import numpy as np

from huygens.interf import c_vector

__all__=['simulate','probability']

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
  means=c_vector(ct.c_double,num_itr)
  _simulate(num_pads,num_itr,means)
  
  return np.ctypeslib.as_array(means)

def probability(num_pads,num_itr):
  return _probability(ct.c_int(num_pads),ct.c_int(num_itr))

def harmonic(n):
  try:
    return _harmonic(ct.c_int(n))
  except WindowsError:
    raise TypeError('`n` must be a positive integer.')
