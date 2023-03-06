import { sumOfDivisors } from "../utils";

const isAbundant = (n: number): boolean => {
  return sumOfDivisors(n) - n > n;
};

const isAbundantSum = (n: number, abundant: Set<number>): boolean => {
  for (const a of abundant) {
    if (a > n / 2) {
      return false;
    }

    if (abundant.has(n - a)) {
      return true;
    }
  }
  return false;
};

export const solve = (): string => {
  const abundant = new Set<number>();
  let nonAbundantSum = 0;
  for (let i = 1; i <= 28123; i++) {
    if (isAbundant(i)) {
      abundant.add(i);
    }

    if (!isAbundantSum(i, abundant)) {
      nonAbundantSum += i;
    }
  }
  return nonAbundantSum.toString();
};
