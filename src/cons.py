#!/usr/bin/env python3.6
import argparse
import math
import numpy as np
import utils

from scipy import stats


def main(args):
  cs = []
  for tag, data in utils.fasta():
    cs.append(list(data))

  X = np.array(cs)
  cons = ''.join(stats.mode(X, axis=0).mode[0])
  print(cons)
  for b in 'ACGT':
    print(f'{b}:', ' '.join(str(x) for x in np.sum(X == b, axis=0)))





if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
