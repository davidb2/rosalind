#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def merge(A, B):
  n, m = len(A), len(B)
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
  return C


def msort(A):
  if len(A) == 1: return A
  return merge(msort(A[:len(A)//2]), msort(A[len(A)//2:]))


def main(args):
  n = int(input())
  A = list(map(int, input().split()))

  print(' '.join(map(str, msort(A))))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
