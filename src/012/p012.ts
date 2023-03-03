import { countOfDivisors } from "../utils";

const triangleNumbers = function* () {
  for (let t = 0, n = 1; ; n++) {
    t += n;
    yield t;
  }
};

export const solve = (): string => {
  for (const t of triangleNumbers()) {
    if (countOfDivisors(t) > 500) {
      return t.toString();
    }
  }
  throw new Error("No solution found");
};
