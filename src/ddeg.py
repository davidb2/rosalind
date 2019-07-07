#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def main(args):
  v, e = tuple(map(int, input().split()))

  es = {u: set() for u in range(1, v+1)}
  for _ in range(e):
    a, b = tuple(map(int, input().split()))
    es[a].add(b)
    es[b].add(a)

  print(' '.join(map(str, (sum(len(es[w]) for w in es[u]) for u in range(1, v+1)))))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
