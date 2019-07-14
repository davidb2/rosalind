#!/usr/bin/env python3.6
import argparse
import math
import numpy as np
import heapq


def main(args):
  n = int(input())
  A = list(map(int, input().split()))
  k = int(input())

  heap = []
  for e in A:
    if len(heap) < k:
      heapq.heappush(heap, -e)
    elif -e > heap[0]:
      heapq.heapreplace(heap, -e)

  print(' '.join(map(str, sorted([-e for e in heap]))))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
