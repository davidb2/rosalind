import os
import sys

from pathlib import Path


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


def pprint(x):
  if type(x) is list:
    print(' '.join(map(str, x)))
  else:
    print(x)
