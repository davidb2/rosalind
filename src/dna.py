from collections import Counter

ELEMENTS = 'ACGT'

counter = Counter(input())
print(' '.join(str(counter[element]) for element in ELEMENTS))
