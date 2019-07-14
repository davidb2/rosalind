#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

from collections import defaultdict


def sp(u, es, dist):
  if u == 1: return 0
  if u not in dist:
    dist[u] = min([es[u][w] + sp(w, es, dist) for w in es[u]] or [+np.inf])
  return dist[u]


def main(args):
  v, e = tuple(map(int, input().split()))

  es = defaultdict(dict)
  for _ in range(e):
    a, b, w = tuple(map(int, input().split()))
    # Invert edges!
    es[b][a] = w

  dist = {}
  ans = [sp(u, es, dist) for u in range(1, v+1)]
  print(' '.join([str(x) if x != np.inf else 'x' for x in ans]))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
