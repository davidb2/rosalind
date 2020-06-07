#!/usr/bin/env python3.6
import argparse
import operator as op

from collections import defaultdict
from functools import reduce


def reach(u, es, seen):
  if u in seen: return set()
  seen.add(u)
  reachable = {u}
  for v in es[u]:
    reachable |= reach(v, es, seen)
  return reachable


def merge(rs):
  for i in range(len(rs)):
    for j in range(i+1, len(rs)):
      us, r1 = rs[i]
      vs, r2 = rs[j]
      if any(v in r1 for v in vs) and any(u in r2 for u in us):
        return [x for k, x in enumerate(rs) if k not in (i, j)] + [(us | vs, r1 | r2)]
  return None


def pathFrom(i, j, es, sccs):
  a = sccs[i]
  b = sccs[j]
  return reduce(lambda x,y: x|y, map(lambda u: es[u], a)) & b


def connected(v, es):
  cc = 0
  seen = set()

  for u in range(1, v+1):
    if u in seen: continue
    dfs = [u]
    while dfs:
      top = dfs.pop()
      if top in seen: continue
      seen.add(top)
      dfs.extend([w for w in es[top]])
    cc += 1

  return cc == 1


def main(args):
  k = int(input())

  for _ in range(k):
    input()
    v, e = tuple(map(int, input().split()))

    es = defaultdict(set)
    bs = defaultdict(set)
    for _ in range(e):
      a, b = tuple(map(int, input().split()))
      es[a].add(b)
      bs[a].add(b)
      bs[b].add(a)

    rs = [({u}, reach(u, es, set())) for u in range(1, v+1)]

    while True:
      rs2 = merge(rs)
      if rs2 is None: break
      rs = rs2

    sccs = [s for s, _ in rs]

    ess = defaultdict(set)
    for i, a in enumerate(sccs):
      for j, b in enumerate(sccs):
        if i == j: continue
        if pathFrom(i, j, es, sccs):
          ess[i].add(j)

    if not connected(v, bs):
      print(-1, end=' ')
    elif not all(len(ess[u]) == 1 for u in ess):
      print(-1, end=' ')
    elif len(reduce(lambda x,y: x|y, map(lambda u: ess[u], ess))) != len(ess):
      print(-1, end=' ')
    else:
      print(+1, end=' ')




if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
