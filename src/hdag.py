#!/usr/bin/env python3.6
import argparse

from queue import Queue


def ts(v, e, indeg, outdeg):
  unseen = set(range(1, v+1))
  ans = []
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
    ans.append(top)

  return ans

def findHP(dp, outdeg):
  m = max(dp[1:])
  i = [j+1 for j, e in enumerate(dp[1:]) if e == m][0]

  ans = [i]
  while dp[i] > 0:
    m = max(dp[e] for e in outdeg[i])
    i = [e for e in outdeg[i] if dp[e] == m][0]
    ans.append(i)

  return ans


def main(args):
  k = int(input())

  for _ in range(k):
    input()

    v, e = tuple(map(int, input().split()))

    indeg = {u: set() for u in range(1, v+1)}
    outdeg = {u: set() for u in range(1, v+1)}
    for _ in range(e):
      a, b = tuple(map(int, input().split()))
      indeg[b].add(a)
      outdeg[a].add(b)

    s = ts(v, e, indeg, outdeg)

    dp = [None] * (v+1)
    for u in reversed(s):
      if len(outdeg[u]) == 0:
        dp[u] = 0
      else:
        dp[u] = 1 + max(dp[z] for z in outdeg[u])

    print(' '.join(map(str, [1] + findHP(dp, outdeg))) if max(dp[1:]) == v - 1 else -1)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
