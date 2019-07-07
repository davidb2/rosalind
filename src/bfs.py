#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

from queue import Queue


def main(args):
  v, e = tuple(map(int, input().split()))

  es = {u: set() for u in range(1, v+1)}
  for _ in range(e):
    a, b = tuple(map(int, input().split()))
    es[a].add(b)

  bfs = Queue()
  seen = set()

  ans = [-1] * (v+1)
  bfs.put((1, 0))

  while not bfs.empty():
    (top, length) = bfs.get()

    if top in seen: continue
    seen.add(top)
    ans[top] = length

    for neighbor in es[top]:
      bfs.put((neighbor, length+1))

  print(' '.join(map(str, ans[1:])))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
