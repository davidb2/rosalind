#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def main(args):
  n = int(input())
  A = eval(input())
  B = eval(input())
  print(A | B)
  print(A & B)
  print(A - B)
  print(B - A)
  print(set(range(1, n+1)) - A)
  print(set(range(1, n+1)) - B)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
