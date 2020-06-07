#!/usr/bin/env python3.6
import argparse
import regex as re
import sys
import threading
import urllib.request

import utils

from collections import defaultdict


PATTERN = re.compile(r'N(?!P).(S|T)(?!P).')
SITE = 'http://www.uniprot.org/uniprot/{}.fasta'


def getInfo(info, uniprotID):
  with urllib.request.urlopen(SITE.format(uniprotID)) as f:
    p = None
    for tag, protein in utils.fasta(fin=f):
      p = protein
      break

    assert p is not None

    matches = re.finditer(PATTERN, p, overlapped=True)
    for m in matches:
      info[uniprotID].append(1+m.start(0))


def main(args):
  ids = []
  for uniprotID in sys.stdin:
    ids.append(uniprotID.rstrip(utils.NEWLINE))

  ts = []
  info = defaultdict(list)
  for uniprotID in ids:
    ts.append(threading.Thread(target=getInfo, args=(info, uniprotID,)))
    ts[-1].start()

  for t in ts:
    t.join()

  for uniprotID in ids:
    if uniprotID in info:
      print(uniprotID)
      utils.pprint(info[uniprotID])


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  args = parser.parse_args()
  main(args)
