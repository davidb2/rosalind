
def gen(xs, n, acc):
  if n == 0:
    yield acc
    return

  for x in xs:
    acc.append(x)
    yield from gen(xs, n-1, acc)
    acc.pop()

if __name__ == '__main__':
  xs = input().split()
  n = int(input())
  for g in gen(xs, n, []):
    print(''.join(g))
