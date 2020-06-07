#!/usr/bin/env pypy
import argparse

from collections import defaultdict

def find(A):
  d = defaultdict(set)
  for i, e in enumerate(A):
    d[e].add(i)

  for i, e in enumerate(A):
    for j, f in enumerate(A):
      if i >= j: continue

      if -(e+f) in d and len(d[-(e+f)] - {i, j}) > 0:
        print '{} {} {}'.format(i+1, j+1, 1+list(d[-(e+f)] - {i, j})[0])
        return

  print str(-1)


def main(args):
  k, n = tuple(map(int, raw_input().split()))
  for _ in range(k):
    A = list(map(int, raw_input().split()))
    find(A)

# For some reason, this code runs very slowly, so I used pypy. O(n^2).
if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
