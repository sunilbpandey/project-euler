import { divide } from "../utils";

export const solve = (): string => {
  const n = 600851475143;

  let largestFactor = 0;
  let result = divide(n, 2);
  if (result.exponent > 0) {
    largestFactor = 2;
  }

  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    result = divide(result.remainder, i);
    if (result.exponent > 0) {
      largestFactor = i;
    }
  }
  return largestFactor.toString();
};
