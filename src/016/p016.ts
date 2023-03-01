import { digitSum } from "../utils";

export const solve = (): string => {
  return digitSum(BigInt(2) ** BigInt(1000)).toString();
};
