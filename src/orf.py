#!/usr/bin/env python3.6
import argparse

import utils

from collections import defaultdict


def matches(xs, m):
  ans = []
  for i in range(len(xs)):
    if utils.RNA_CODON_TABLE.get(xs[i:i+3]) == m:
      ans.append(i)
  return ans


def main(args):
  _, dna = next(utils.fasta())
  cp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
  rna = dna.replace('T', 'U')
  rrna = ''.join([cp[b] for b in dna]).replace('T', 'U')[::-1]

  proteins = set()
  for r in (rna, rrna):
    starts = matches(r, 'M')
    ends = matches(r, 'Stop')
    for s in starts:
      j = min([i for i, x in enumerate(ends) if (x % 3) == (s % 3) and x > s] or [-1])
      if j == -1: continue
      e = ends[j]
      proteins.add(''.join([utils.RNA_CODON_TABLE[r[i:i+3]] for i in range(s, e, 3)]))

  for protein in proteins:
    print(protein)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
