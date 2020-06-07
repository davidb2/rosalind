#!/usr/bin/env python3.6
from collections import defaultdict
import sys

def cc(vertices, edges):
  seen = set()

  n = 0
  for vertex in vertices:
    if vertex not in seen:
      q = [vertex]
      while q:
        u = q.pop()
        if u in seen: continue
        seen.add(u)
        q.extend(edges[u])
      n += 1
  return n

if __name__ == '__main__':
  n = int(input())
  vertices = set(range(1, n+1))
  edges = defaultdict(set)

  for line in sys.stdin.readlines():
    u, v = map(int, line.strip().split())
    edges[u].add(v)
    edges[v].add(u)

  components = cc(vertices, edges)
  print(components - 1)
