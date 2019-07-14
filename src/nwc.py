#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

from collections import defaultdict


def update(u, v, es, dist):
  dist[v] = min(dist[v], dist[u] + es[u][v])


def main(args):
  k = int(input())

  for _ in range(k):
    v, e = tuple(map(int, input().split()))

    dist = defaultdict(lambda: np.inf)
    es = defaultdict(dict)
    for _ in range(e):
      a, b, w = tuple(map(int, input().split()))
      es[a][b] = w

    for x in range(1, v+1):
      es[0][x] = 0

    dist[0] = 0

    for _ in range(v-1):
      for u, zs in es.items():
        for z in zs:
          update(u, z, es, dist)


    ans = [dist[x] for x in range(1, v+1)]

    for u, zs in es.items():
      for z in zs:
        update(u, z, es, dist)

    ans2 = [dist[x] for x in range(1, v+1)]

    print(+1 if ans != ans2 else -1, end=' ')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
