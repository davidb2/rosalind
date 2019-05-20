#!/usr/bin/env python3.6
import argparse
import functools
import itertools
import scipy.stats.distributions
import sys


POSSIBLE_GENOTYPES = [
  tuple(''.join(gene) for gene in genotype)
  for genotype in itertools.product(
    itertools.combinations_with_replacement('Aa', 2),
    itertools.combinations_with_replacement('Bb', 2),
  )
]

@functools.lru_cache(maxsize=None)
def Pr(child: tuple, parent: tuple) -> float:
  '''
  Parent always mates with ('Aa', 'Bb') genotype.
  Example:
    parent:  ['Aa', 'Bb']
    child:   ['Aa', 'Bb']
    returns: 4/16 = 0.25
  '''
  toSets = lambda genotype: [sorted(gene) for gene in genotype]
  parent1 = toSets(parent)
  parent2 = toSets(('Aa', 'Bb'))
  child1 = toSets(child)

  assert len(parent1) == len(parent2) == len(child1)

  zipped = [
    itertools.product(gene1, gene2)
    for gene1, gene2 in zip(parent1, parent2)
  ]

  possibleOutcomes = [
    toSets(gene)
    for gene in itertools.product(*zipped)
  ]

  return possibleOutcomes.count(child1) / len(possibleOutcomes)

@functools.lru_cache(maxsize=None)
def P(i, g):
  '''
  Probability of genotype g at level i.
  '''
  if i == 0 and g == ('Aa', 'Bb'): return 1.
  elif i <= 0: return 0.
  return sum(
    Pr(g, gp) * P(i-1, gp)
    for gp in POSSIBLE_GENOTYPES
  )

@functools.lru_cache(maxsize=None)
def atLeast(N, k):
  '''
  Probability of at least N ('Aa', 'Bb') genotypes at level k.
  '''
  binom = scipy.stats.distributions.binom
  # P(k, ('Aa', 'Bb')) is always 0.25 for k > 0 due to independence.
  return 1. - binom.cdf(N-1, n=2**k, p=P(k, ('Aa', 'Bb')))

def main(args):
  N, k = args.N, args.k
  print(atLeast(N, k))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-N', type=int, required=True)
  parser.add_argument('-k', type=int, required=True)
  args = parser.parse_args()
  sys.setrecursionlimit((1<<31)-1)
  main(args)
