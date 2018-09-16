#!/usr/bin/env python3.6

FILE = 'datasets/rna.txt'

def main():
  with open(FILE, 'r') as f:
    print(''.join('U' if element == 'T' else element for element in f.read()))

if __name__ == '__main__':
  main()
