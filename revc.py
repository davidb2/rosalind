translationTable = str.maketrans('ACGT', 'TGCA')
print(str.translate(input()[::-1], translationTable))
