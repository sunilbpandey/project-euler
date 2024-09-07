import { fibonacci } from "../utils";

export const solve1 = (): string => {
  let index = 0;
  for (const n of fibonacci()) {
    index++;
    if (n.toString().length >= 1000) {
      break;
    }
  }
  return index.toString();
};

export const solve = (): string => {
  const phi = (1 + Math.sqrt(5)) / 2;
  const n = (999 * Math.log(10) + Math.log(5) / 2) / Math.log(phi);
  return Math.round(n).toString();
};
