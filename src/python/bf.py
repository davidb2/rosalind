#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

from collections import defaultdict


def update(u, v, es, dist):
  dist[v] = min(dist[v], dist[u] + es[u][v])


def main(args):
  v, e = tuple(map(int, input().split()))

  dist = defaultdict(lambda: np.inf)
  es = defaultdict(dict)
  for _ in range(e):
    a, b, w = tuple(map(int, input().split()))
    es[a][b] = w

  dist[1] = 0

  for _ in range(v-1):
    for u, zs in es.items():
      for z in zs:
        update(u, z, es, dist)

  for x in range(1, v+1):
    print(dist[x] if dist[x] != np.inf else 'x', end=' ')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
