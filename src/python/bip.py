#!/usr/bin/env python3.6
import argparse

from queue import Queue

def bip(v, e, es):
  seen = {}
  for u in range(1, v+1):
    if u in seen: continue

    bfs = Queue()
    bfs.put((u, 0))
    while not bfs.empty():
      top, c = bfs.get()

      if top in seen:
        if seen[top] != c: return False
        else: continue

      seen[top] = c
      for neighbor in es[top]:
        bfs.put((neighbor, 1-c))

  return True


def main(args):
  k = int(input())
  ans = []

  for _ in range(k):
    input()
    v, e = tuple(map(int, input().split()))

    es = {u: set() for u in range(1, v+1)}
    for _ in range(e):
      a, b = tuple(map(int, input().split()))
      es[a].add(b)
      es[b].add(a)

    ans.append(+1 if bip(v, e, es) else -1)

  print(' '.join(map(str, ans)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
