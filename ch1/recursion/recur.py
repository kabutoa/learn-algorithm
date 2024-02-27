def recur(n: int) -> int:
  if n == 1:
    return 1
  return n + recur(n - 1)

print(recur(10))