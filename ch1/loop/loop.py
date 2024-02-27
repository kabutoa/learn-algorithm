def forLoop(n: int) -> int:
  sum = 0
  for i in range(1, n + 1):
    sum += i
  return sum

print(forLoop(10))