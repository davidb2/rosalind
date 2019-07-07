#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def main(args):
  n = int(input())
  A = list(map(int, input().split()))

  numSwaps = 0
  for i in range(1, n):
    k = i
    while k > 0 and A[k] < A[k-1]:
      A[k], A[k-1] = A[k-1], A[k]
      k -= 1
      numSwaps += 1

  print(numSwaps)



if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
