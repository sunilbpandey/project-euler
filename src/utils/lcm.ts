import { gcd } from "./gcd";

export const lcm = (a: number, b: number): number => {
  return a * (b / gcd(a, b));
};
