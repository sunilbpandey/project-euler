export const solve1 = (): string => {
  for (let a = 1; a < 333; a++) {
    const numerator = 1000 * (500 - a);
    const denominator = 1000 - a;

    if (numerator % denominator === 0) {
      const b = numerator / denominator;

      // Since we know this is the only solution, we can stop here
      return (a * b * (1000 - a - b)).toString();
    }
  }
  throw new Error("No solution found");
};

export const solve = (): string => {
  for (let m = 1; m < 22; m++) {
    for (let n = 1; n < m; n++) {
      if (m * (m + n) === 500) {
        const a = m * m - n * n;
        const b = 2 * m * n;
        const c = m * m + n * n;

        return (a * b * c).toString();
      }
    }
  }
  throw new Error("No solution found");
};
