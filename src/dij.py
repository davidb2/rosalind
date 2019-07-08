#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

from collections import defaultdict
from queue import PriorityQueue


def main(args):
  v, e = tuple(map(int, input().split()))

  es = defaultdict(dict)
  for _ in range(e):
    a, b, w = tuple(map(int, input().split()))
    es[a][b] = w

  bfs = PriorityQueue()
  seen = set()

  ans = [-1] * (v+1)
  bfs.put((0, 1))

  while not bfs.empty():
    (length, top) = bfs.get()

    if top in seen: continue
    seen.add(top)
    ans[top] = length

    for neighbor in es[top]:
      bfs.put((length+es[top][neighbor], neighbor))

  print(' '.join(map(str, ans[1:])))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
