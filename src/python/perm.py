#!/usr/bin/env python3.6
import argparse
import itertools

def main(args):
  n = args.n

  perms = [' '.join(map(str, perm)) for perm in itertools.permutations(range(1, n+1))]
  print(len(perms))
  print('\n'.join(perms))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, required=True)
  args = parser.parse_args()
  main(args)
