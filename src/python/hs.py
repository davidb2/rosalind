#!/usr/bin/env python3.6
import argparse
import copy
import math
import numpy as np

def sat(A):
  for i in range(2, len(A)):
    if not (A[i // 2] <= A[i]):
      print(A[i // 2], A[i], i // 2, i)


def siftDown(A, k):
  js = []
  while k >= 2:
    js.append(k)
    k //= 2

  for j in reversed(js):
    if not (A[j // 2] <= A[j]):
      A[j], A[j // 2] = A[j // 2], A[j]


def sift(A):
  k = 1
  while k < len(A):
    if 2*k < len(A) and 2*k+1 < len(A):
      if A[k] <= A[2*k] and A[k] <= A[2*k+1]: break
      elif A[2*k] < A[2*k+1]:
        A[k], A[2*k] = A[2*k], A[k]
        k = 2*k
      else:
        A[k], A[2*k+1] = A[2*k+1], A[k]
        k = 2*k+1
    elif 2*k < len(A) and A[2*k] < A[k]:
        A[k], A[2*k] = A[2*k], A[k]
        k = 2*k
    else:
      break


def heapify(A):
  for i in reversed(range(2, len(A))):
    siftDown(A, i)


def hsort(A):
  B = []
  C = copy.deepcopy(A)

  while len(C) >= 2:
    C[-1], C[1] = C[1], C[-1]
    B.append(C.pop())
    if len(C) <= 1: break
    sift(C)

  return B


def main(args):
  n = int(input())
  A = [None] + list(map(int, input().split()))

  heapify(A)
  B = hsort(A)

  print(' '.join(map(str, B)))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
