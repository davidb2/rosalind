#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

def sat(A):
  for i in range(2, len(A)):
    if not (A[i // 2] >= A[i]):
      print(A[i // 2], A[i], i // 2, i)

def main(args):
  n = int(input())
  A = [None] + list(map(int, input().split()))

  for i in reversed(range(2, n+1)):
    k = i
    js = []
    while k >= 2:
      js.append(k)
      k //= 2

    for j in reversed(js):
      if not (A[j // 2] >= A[j]):
        A[j], A[j // 2] = A[j // 2], A[j]

  print(' '.join(map(str, A[1:])))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
