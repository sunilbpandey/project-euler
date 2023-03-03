import { arraySum, divisors, range, sumOfDivisors } from "../utils";

const properDivisors = (n: number): number[] =>
  divisors(n).filter((d) => d !== n);

const sumOfProperDivisors1 = (n: number): number => arraySum(properDivisors(n));

const sumOfProperDivisors = (n: number): number => sumOfDivisors(n) - n;

const isAmicable = (n: number): boolean => {
  const m = sumOfProperDivisors(n);
  return m !== n && sumOfProperDivisors(m) === n;
};

export const solve = (): string => {
  return arraySum(range(2, 10001).filter(isAmicable)).toString();
};
