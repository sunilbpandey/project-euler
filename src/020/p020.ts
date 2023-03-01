import { digitSum, factorial } from "../utils";

export const solve = (): string => {
  return digitSum(factorial(100)).toString();
};
