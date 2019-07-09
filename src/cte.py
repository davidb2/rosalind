#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

from collections import defaultdict
from queue import PriorityQueue

def short(start, end, v, e, es):
  bfs = PriorityQueue()
  bfs.put((0, start))

  seen = set()
  while not bfs.empty():
    length, top = bfs.get()

    if top == end: return length + es[end][start]
    if top in seen: continue
    seen.add(top)

    for u in es[top]:
      bfs.put((length+es[top][u], u))

  return -1

def main(args):
  k = int(input())

  for _ in range(k):

    v, e = tuple(map(int, input().split()))

    es = defaultdict(dict)
    start, end = None, None
    for _ in range(e):
      a, b, w = tuple(map(int, input().split()))
      if start is None and end is None:
        start, end = a, b
      es[a][b] = w

    print(short(end, start, v, e, es), end=' ')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
