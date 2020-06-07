#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def main(args):
  n = int(input())
  A = list(map(int, input().split()))

  q = A[0]
  B = [x for x in A if x < q] + [x for x in A if x == q] + [x for x in A if x > q]

  print(' '.join(map(str, B)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
