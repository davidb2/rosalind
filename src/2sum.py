#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

from collections import defaultdict


def main(args):
  k, n = tuple(map(int, input().split()))
  for _ in range(k):
    d = defaultdict(set)
    A = list(map(int, input().split()))
    for i, e in enumerate(A):
      d[e].add(i)

    for i, e in enumerate(A):
      if -e in d and len(d[-e] - {i}) > 0:
        print(i+1, 1+list(d[-e] - {i})[0])
        break
    else:
      print(-1)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
