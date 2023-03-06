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
  let sum = 0;
  let d = 1;
  for (; d ** 2 < n; d++) {
    if (n % d === 0) {
      sum += d + n / d;
    }
  }

  if (d ** 2 === n) {
    sum += d;
  }
  return sum;
};
