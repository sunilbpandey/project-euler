export const solve = (): string => {
  return Array.from({ length: 999 }, (_, i) => i + 1)
    .filter((n) => n % 3 === 0 || n % 5 === 0)
    .reduce((prev, cur) => prev + cur)
    .toString();
};
