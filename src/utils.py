import os
import sys

from itertools import islice
from pathlib import Path


RNA_CODON_TABLE = {
  'UUU': 'F',
  'UUC': 'F',
  'UUA': 'L',
  'UUG': 'L',
  'UCU': 'S',
  'UCC': 'S',
  'UCA': 'S',
  'UCG': 'S',
  'UAU': 'Y',
  'UAC': 'Y',
  'UAA': 'Stop',
  'UAG': 'Stop',
  'UGU': 'C',
  'UGC': 'C',
  'UGA': 'Stop',
  'UGG': 'W',
  'CUU': 'L',
  'CUC': 'L',
  'CUA': 'L',
  'CUG': 'L',
  'CCU': 'P',
  'CCC': 'P',
  'CCA': 'P',
  'CCG': 'P',
  'CAU': 'H',
  'CAC': 'H',
  'CAA': 'Q',
  'CAG': 'Q',
  'CGU': 'R',
  'CGC': 'R',
  'CGA': 'R',
  'CGG': 'R',
  'AUU': 'I',
  'AUC': 'I',
  'AUA': 'I',
  'AUG': 'M',
  'ACU': 'T',
  'ACC': 'T',
  'ACA': 'T',
  'ACG': 'T',
  'AAU': 'N',
  'AAC': 'N',
  'AAA': 'K',
  'AAG': 'K',
  'AGU': 'S',
  'AGC': 'S',
  'AGA': 'R',
  'AGG': 'R',
  'GUU': 'V',
  'GUC': 'V',
  'GUA': 'V',
  'GUG': 'V',
  'GCU': 'A',
  'GCC': 'A',
  'GCA': 'A',
  'GCG': 'A',
  'GAU': 'D',
  'GAC': 'D',
  'GAA': 'E',
  'GAG': 'E',
  'GGU': 'G',
  'GGC': 'G',
  'GGA': 'G',
  'GGG': 'G',
}
NEWLINE = os.linesep
TAG = '>'


def fasta(fin=sys.stdin):
  try:
    providedFileName = type(fin) is str
    if providedFileName:
      fin = Path(fin).open()

    found = False
    tag = None
    data = []
    for datum in fin:
      if type(datum) is bytes:
        datum = datum.decode('utf-8')
      if not datum.startswith(TAG):
        if tag is not None:
          data.append(datum.rstrip(NEWLINE))
      else:
        if tag is not None:
          yield (tag, ''.join(data))
          found = True
          data.clear()
        tag = datum[1:].rstrip(NEWLINE)

    if data:
      yield (tag, ''.join(data))
      found = True

    if not found:
      yield from ()

  finally:
    if providedFileName:
      fin.close()


def fastaN(n, *args, **kwargs):
  return list(islice(fasta(*args, **kwargs), n))


def pprint(x):
  if type(x) is list:
    print(' '.join(map(str, x)))
  else:
    print(x)

