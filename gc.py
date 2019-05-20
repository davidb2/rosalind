import sys

strings = []

currentLabel = None
currentString = []
for line in sys.stdin:
  if line.startswith('>'):
    if currentLabel is not None:
      strings.append((currentLabel.replace('\n', ''), ''.join(currentString).replace('\n', '')))
    currentLabel = line[1:]
    currentString = []
  else:
    currentString.append(line)
if currentString and currentLabel:
  strings.append((currentLabel.replace('\n', ''), ''.join(currentString).replace('\n', '')))

def gcContent(string):
  return (string.count('C') + string.count('G')) / float(len(string))

label, string = max(strings, key=lambda t: gcContent(t[1]))
print(label)
print(100 * gcContent(string))
