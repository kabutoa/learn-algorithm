const forLoop = (n: number) => {
  let sum = 0;
  for (let i = 0; i <= n; i++) {
    sum += i;
  }
  return sum;
};

console.log(forLoop(10));
