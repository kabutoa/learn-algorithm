def whileLoop(n: int) -> int:
  sum = 0
  i = 1
  while i <= n:
    sum += i
    i += 1
  return sum

print(whileLoop(10))