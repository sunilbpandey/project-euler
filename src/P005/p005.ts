import { lcm } from "../utils";

export const solve = (): string => {
  let smallestMultiple = 1;
  for (let i = 2; i <= 20; i++) {
    smallestMultiple = lcm(smallestMultiple, i);
  }
  return smallestMultiple.toString();
};
