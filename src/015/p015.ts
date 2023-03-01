import { factorial } from "../utils";

export const solve = (): string => {
  const n = 20;
  return (factorial(2 * n) / (factorial(n) * factorial(n))).toString();
};
