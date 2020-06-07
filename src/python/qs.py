#!/usr/bin/env python3.6
import argparse
import math
import numpy as np
import random

def qsort(A):
  if len(A) <= 1: return A
  i = random.randint(0, len(A)-1)
  q = A[i]
  left = [x for x in A if x < q]
  mid = [x for x in A if x == q]
  right = [x for x in A if x > q]
  return qsort(left) + mid + qsort(right)


def main(args):
  n = int(input())
  A = list(map(int, input().split()))

  print(' '.join(map(str, qsort(A))))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
