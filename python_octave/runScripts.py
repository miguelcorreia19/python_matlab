import os, datetime
from oct2py import Oct2Py
import numpy as np

def processFactorial(number):
  oc = Oct2Py()
  oc.addpath('./scriptsMatlab') # Add Matlab/Octave scripts path

  result = oc.factorial(number, nout=1) # nout is the number of output parameters
  return result

def processFibonacci(number):
  oc = Oct2Py()
  oc.addpath('./scriptsMatlab') # Add Matlab/Octave scripts path

  result = oc.fibonacci(number, nout=1) # nout is the number of output parameters
  return result[0].tolist()