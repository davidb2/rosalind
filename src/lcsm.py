#!/usr/bin/env python3.6
import argparse
import math
import numpy as np
import utils

from functools import reduce
from scipy import stats


def ds(xs, l):
  return set(xs[i:i+l] for i in range(len(xs)))

def lcs(cs, l):
  return max(reduce(lambda x,y: x&y, (ds(xs, l) for xs in cs)) or [''], key=len)


def main(args):
  cs = []
  for tag, data in utils.fasta():
    cs.append(data)

  lo = 0
  hi = 1000
  while True:
    if hi - lo < 4:
      for l in reversed(range(lo, hi+1)):
        lc = lcs(cs, l)
        if lc:
          print(lc)
          break
      return
    else:
      mid = (lo + hi) // 2
      if lcs(cs, mid):
        lo = mid
      else:
        hi = mid




if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
