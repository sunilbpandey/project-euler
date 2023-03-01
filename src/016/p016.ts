import { arraySum } from "../utils";

const digitSum = (n: number | bigint) => {
  const digits = n
    .toString()
    .split("")
    .map((ch) => parseInt(ch));
  return arraySum(digits);
};

export const solve = (): string => {
  return digitSum(BigInt(2) ** BigInt(1000)).toString();
};
