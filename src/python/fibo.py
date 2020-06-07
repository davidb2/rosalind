#!/usr/bin/env python3.6
import argparse
import math
import numpy as np


def main(args):
  a, b = 0, 1
  for _ in range(args.n):
    a, b = b, a+b

  print(a)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, required=True)

  args = parser.parse_args()
  main(args)
