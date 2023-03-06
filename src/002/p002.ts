import { fibonacci } from "../utils";

// Simple implementation using a generator
export const solve1 = (): string => {
  let sum = 0;
  let index = 0;
  for (const n of fibonacci()) {
    if (Number(n) > 4000000) {
      break;
    }

    // Add every third term
    index++;
    if (index % 3 === 0) {
      sum += Number(n);
    }
  }
  return sum.toString();
};

export const solve = (): string => {
  let sum = 0;
  for (let a = 1, b = 1; a + b < 4000000; ) {
    const c = a + b;
    a = b + c;
    b = c + a;
    sum += c;
  }
  return sum.toString();
};
