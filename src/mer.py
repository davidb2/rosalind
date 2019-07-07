#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def main(args):
  n = int(input())
  A = list(map(int, input().split()))
  m = int(input())
  B = list(map(int, input().split()))

  C = []
  i, j = 0, 0
  for _ in range(n+m):
    if j >= m:
      C.append(A[i])
      i += 1
    elif i >= n:
      C.append(B[j])
      j += 1
    elif A[i] < B[j]:
      C.append(A[i])
      i += 1
    else:
      C.append(B[j])
      j += 1

  print(' '.join(map(str, C)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
