#!/usr/bin/env python3.6
import argparse

MOD = 10 ** 6

def main(args):
  print(pow(2, args.n, MOD))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, required=True)
  args = parser.parse_args()
  main(args)
