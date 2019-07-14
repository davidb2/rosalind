#!/usr/bin/env python3.6
import argparse
import operator as op
import sys

from collections import defaultdict


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
  sys.setrecursionlimit(10**6)
  k = int(input())

  for _ in range(k):
    input()

    v, e = tuple(map(int, input().split()))

    es = defaultdict(set)
    for _ in range(e):
      a, b = tuple(map(int, input().split()))
      es[-a].add(b)
      es[-b].add(a)

    n = 2*v
    m = 2*e
    rs = [(u, reach(u, es, set())) for u in list(range(-v, 0)) + list(range(1, v+1))]

    while True:
      rs2 = merge(rs)
      if rs2 is None: break
      rs = rs2

    sccs = rs
    for _, scc in sccs:
      if len(set(map(abs, scc))) < len(scc):
        print(0)
        break
    else:
      assignments = {}
      print(sccs)
      while len(sccs) > 0:
        for i in range(len(sccs)):
          _, scc = sccs[i]
          for u in scc:
            if len(es[u] & scc) != len(es[u]): break
          else:
            for u in scc:
              assignments[u] = True
              assignments[-u] = False
              for j, (_, oscc) in enumerate(sccs):
                if j != i:
                  oscc.discard(u)
                  oscc.discard(-u)
            del sccs[i]
          break
      ans = sorted((u for u, a in assignments.items() if a), key=abs)
      # print(ans, len(ans))
      print(1, ' '.join(map(str, ans)))




if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
