#!/usr/bin/env python3.6
import argparse
import numpy as np

from utils import fasta


if __name__ == '__main__':
  words = []
  for tag, line in fasta():
    words.append(line)
  assert len(words) == 2, len(words)

  A, B = words
  print(A, B)
  n = len(A)
  m = len(B)
  E = np.zeros((n+1, m+1), dtype=np.int32)
  for i in range(n+1):
    for j in range(m+1):
      if i == j == 0: continue
      E[i, j] = min(
        1 + E[i, j-1] if j > 0 else np.inf,
        1 + E[i-1, j] if i > 0 else np.inf,
        (int(A[i-1] != B[j-1]) + E[i-1, j-1]) if i > 0 and j > 0 else np.inf
      )
  print(E)
  print(E[n,m])
