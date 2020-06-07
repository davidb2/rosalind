#!/usr/bin/env python3.6
import argparse
import math


def main(args):
  dna = input()
  gcs = list(map(float, input().split()))

  print(' '.join(map(str, [
    sum(math.log(p/2. if bb in 'GC' else (1-p)/2., 10) for bb in dna)
    for b, p in zip(dna, gcs)
  ])))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
