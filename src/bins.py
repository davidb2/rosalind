#!/usr/bin/env python3.6
import argparse
import bisect
import numpy as np


def main(args):
  n = int(input())
  m = int(input())
  A = list(map(int, input().split()))
  ks = list(map(int, input().split()))

  ans = [bisect.bisect(A, k) for k in ks]
  rans = [i if A[i-1] == ks[j] else -1 for j, i in enumerate(ans)]
  print(' '.join(list(map(str, rans))))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
