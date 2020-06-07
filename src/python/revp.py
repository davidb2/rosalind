#!/usr/bin/env python3.6
from utils import fastaN

t = dict((('A', 'T'), ('T', 'A'), ('G', 'C'), ('C', 'G')))
def rc(dna):
  return ''.join([t[x] for x in dna][::-1])

if __name__ == '__main__':
  (_, dna), *_ = fastaN(1)

  print('\n'.join([
    f'{p+1} {l}'
    for p in range(len(dna))
    for l in range(4, 12+1)
    if len(dna[p:p+l]) == l and dna[p:p+l] == rc(dna[p:p+l])
  ]))
