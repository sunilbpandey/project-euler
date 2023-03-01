import { arraySum } from "./array";

export const digitSum = (n: number | bigint) => {
  const digits = n
    .toString()
    .split("")
    .map((ch) => parseInt(ch));
  return arraySum(digits);
};
