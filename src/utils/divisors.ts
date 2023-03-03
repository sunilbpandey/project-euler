import { factorize } from "./primeNumbers";
import { range } from "./range";

export const divisors = (n: number): number[] => {
  const limit = Math.floor(Math.sqrt(n));
  const divisors: number[] = [1, n];
  range(2, limit + 1).forEach((d) => {
    if (n % d === 0) {
      divisors.push(d);
      const q = n / d;
      if (q !== d) {
        divisors.push(q);
      }
    }
  });
  return divisors;
};

export const countOfDivisors = (n: number) => {
  return Object.values(factorize(n))
    .map((power) => power + 1)
    .reduce((prev, cur) => prev * cur, 1);
};

export const sumOfDivisors = (n: number): number => {
  const factors = factorize(n);

  let num = 1;
  let den = 1;
  for (const [p, e] of Object.entries(factors)) {
    const prime = parseInt(p);
    num *= prime ** (e + 1) - 1;
    den *= prime - 1;
  }
  return num / den;
};
