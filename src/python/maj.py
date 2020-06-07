#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

def maj(A):
  a, m = A[1], 1
  for e in A[1:]:
    if a == e:
      m += 1
    elif a != e:
      m -= 1
      if m == 0:
        a = e
        m = 1

  return a if A.count(a) > len(A) // 2 else -1

def main(args):
  k, n = tuple(map(int, input().split()))

  ans = []
  for _ in range(k):
    A = list(map(int, input().split()))
    ans.append(maj(A))
  print(' '.join(map(str, ans)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
