const recur = (n: number): number => {
  if (n === 1) return 1;
  return n + recur(n - 1);
};

console.log(recur(10));
