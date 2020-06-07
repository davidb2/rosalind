#!/usr/bin/env python3.6
import argparse

from queue import Queue


def acyclic(v, e, indeg, outdeg):
  unseen = set(range(1, v+1))
  bfs = Queue()

  for u in unseen:
    if len(indeg[u]) == 0:
      bfs.put(u)

  while len(unseen) > 0:
    if bfs.empty(): return False

    top = bfs.get()
    for out in outdeg[top]:
      indeg[out].remove(top)
      if len(indeg[out]) == 0:
        bfs.put(out)

    unseen.remove(top)

  return True


def main(args):
  k = int(input())
  ans = []

  for _ in range(k):
    input()
    v, e = tuple(map(int, input().split()))

    indeg = {u: set() for u in range(1, v+1)}
    outdeg = {u: set() for u in range(1, v+1)}
    for _ in range(e):
      a, b = tuple(map(int, input().split()))
      indeg[b].add(a)
      outdeg[a].add(b)

    ans.append(+1 if acyclic(v, e, indeg, outdeg) else -1)

  print(' '.join(map(str, ans)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
