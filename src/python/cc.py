#!/usr/bin/env python3.6
import argparse
import numpy as np

from queue import Queue


def main(args):
  v, e = tuple(map(int, input().split()))

  es = {u: set() for u in range(1, v+1)}
  for _ in range(e):
    a, b = tuple(map(int, input().split()))
    es[a].add(b)
    es[b].add(a)

  cc = 0
  seen = set()
  for u in range(1, v+1):
    if u in seen: continue

    bfs = Queue()
    bfs.put(u)
    while not bfs.empty():
      top = bfs.get()
      if top in seen: continue
      seen.add(top)
      for neighbor in es[top]:
        bfs.put(neighbor)
    cc += 1

  print(cc)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
