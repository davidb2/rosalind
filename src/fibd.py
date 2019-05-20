n, m = tuple(map(int, input().split()))

def shiftRight(arr):
  if not arr: return
  temp = arr[0]
  for i in range(1, len(arr)):
    temp, arr[i] = arr[i], temp
  arr[0] = 0

young, old = 1, [0] * (m-1)
for month in range(n-1):
  newYoung = sum(old)
  shiftRight(old)
  old[0] = young
  young = newYoung
print(young + sum(old))
