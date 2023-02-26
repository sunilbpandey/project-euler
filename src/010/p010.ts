import { primes } from "../utils";

export const solve = (): string => {
  let sum = 0;
  for (const p of primes()) {
    if (p > 2000000) {
      break;
    }
    sum += p;
  }
  return sum.toString();
};
