from functools import reduce
import operator
import sys

def calcProb(*args):
  z = lambda p: -p if p < 0. else p
  return sum(reduce(operator.mul, map(z, arg)) for arg in args)

k, m, n = tuple(map(float, input().split()))
pop = float(k + m + n)
if pop < 2:
  print(0)
  sys.exit(0)
else:
  print(calcProb(
    [1., k/pop, (m+n)/(pop-1)],
    [1., (m+n)/pop, k/(pop-1)],
    [1., k/pop, (k-1)/(pop-1)],
    [0.75, m/pop, (m-1)/(pop-1)],
    [0.5, m/pop, n/(pop-1)],
    [0.5, n/pop, m/(pop-1)],
  ))
