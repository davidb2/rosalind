n, k = tuple(map(int, input().split()))

young, old = 1, 0
for month in range(n-1):
  young, old = old * k, young + old
print(young + old)
