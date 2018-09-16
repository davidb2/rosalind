#!/usr/bin/env python3.6
from collections import Counter

FILE = 'datasets/dna.txt'
ELEMENTS = 'ACGT'

def main():
    counter = Counter(f.read())
    print(' '.join(str(counter[element]) for element in ELEMENTS))

if __name__ == '__main__':
  main(input())
