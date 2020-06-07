#!/usr/bin/env python3.6
import argparse
import math
import numpy as np
import random


def qselect(A, k):
  if len(A) < 10: return sorted(A)[k]

  i = random.randint(0, len(A)-1)
  q = A[i]
  left = [e for j, e in enumerate(A) if j != i and e <= q]
  right = [e for j, e in enumerate(A) if j != i and q < e]

  if k < len(left):
    return qselect(left, k)
  elif k > len(left):
    return qselect(right, k - len(left) - 1)
  else:
    return q


def main(args):
  n = int(input())
  A = list(map(int, input().split()))
  k = int(input())

  print(qselect(A, k-1))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
