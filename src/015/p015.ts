const factorial = (n: number): number => {
  let fac = 1;
  for (let i = 1; i <= n; i++) {
    fac *= i;
  }
  return fac;
};

export const solve = (): string => {
  const n = 20;
  return (factorial(2 * n) / (factorial(n) * factorial(n))).toString();
};
