import { primes } from "../utils";

export const solve = (): string => {
  let count = 0;
  for (const p of primes()) {
    if (++count === 10001) {
      return p.toString();
    }
  }
  throw new Error("No solution found");
};
