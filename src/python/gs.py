#!/usr/bin/env python3.6
import argparse
import math
import numpy as np

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
      u, r1 = rs[i]
      v, r2 = rs[j]
      if v in r1 and u in r2:
        return [x for k, x in enumerate(rs) if k not in (i, j)] + [(u, r1 | r2)]
  return None


def main(args):
  k = int(input())

  for _ in range(k):
    input()

    v, e = tuple(map(int, input().split()))

    es = defaultdict(set)
    for _ in range(e):
      a, b = tuple(map(int, input().split()))
      es[a].add(b)

    ss = [(u, reach(u, es, set())) for u in range(1, v+1)]
    for u, s in ss:
      if len(s) == v:
        print(u, end=' ')
        break
    else:
      print(-1, end=' ')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
