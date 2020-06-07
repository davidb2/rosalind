#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    self.size = 1 + (left.size if left else 0) + (right.size if right else 0)


def addValue(node, value):
  assert node is not None
  node.size += 1
  if value < node.value:
    if node.left:
      addValue(node.left, value)
    else:
      node.left = Node(value)
  else:
    if node.right:
      addValue(node.right, value)
    else:
      node.right = Node(value)

def numGreater(node, value):
  if node is None: return 0
  elif value < node.value: return 1 + (node.right.size if node.right else 0) + numGreater(node.left, value)
  else: return numGreater(node.right, value)


# Note: This program only works well in the average case. Use a self balancing
# BST for optimal performance. I just guessed that ROSALIND was going to spit
# out a uniformly random list of numbers. O(n^2) worst; O(nlgn) avg.
def main(args):
  n = int(input())
  A = list(map(int, input().split()))

  invs = 0
  t = Node(A[0])
  for e in A[1:]:
    invs += numGreater(t, e)
    addValue(t, e)

  print(invs)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
