#!/usr/bin/env python3.6
import argparse
import itertools
import sys

def fasta():
  strings = []
  currentString = []
  currentLabel = None
  for line in sys.stdin:
    if line.startswith('>'):
      if currentLabel is not None:
        strings.append((currentLabel.replace('\n', ''), ''.join(currentString).replace('\n', '')))
      currentLabel = line[1:]
      currentString = []
    else:
      currentString.append(line)
  if currentString and currentLabel:
    strings.append((currentLabel.replace('\n', ''), ''.join(currentString).replace('\n', '')))
  return strings

def main(args):
  k = args.k

  for (n1, s1), (n2, s2) in itertools.product(fasta(), repeat=2):
    if n1 != n2 and s1[-k:] == s2[:k]:
      print(n1, n2)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-k', type=int, default=3)
  args = parser.parse_args()
  main(args)
