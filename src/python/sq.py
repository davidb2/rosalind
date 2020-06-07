#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def hasSquare(v, e, es, seen):
  if len(seen) == 4 and seen[0] in es[seen[-1]] and len(set(seen)) == 4: return True
  if len(seen) > 4: return False

  for u in es[seen[~0]]:
    seen.append(u)
    if hasSquare(v, e, es, seen): return True
    seen.pop()

  return False

def main(args):
  k = int(input())

  for _ in range(k):
    input()

    v, e = tuple(map(int, input().split()))

    es = {u: set() for u in range(1, v+1)}
    for _ in range(e):
      a, b = tuple(map(int, input().split()))
      es[a].add(b)
      es[b].add(a)

    print(+1 if any(hasSquare(v, e, es, [u]) for u in range(1, v+1)) else -1, end= ' ')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
