export const arrayProduct = (arr: number[]): number =>
  arr.reduce((a, b) => a * b, 1);

export const arraySum = (arr: number[]): number =>
  arr.reduce((a, b) => a + b, 0);
