export const factorial = (n: number): bigint => {
  const numbers = Array.from({ length: n }, (_, i) => BigInt(i + 1));
  return numbers.reduce((acc, cur) => acc * cur, BigInt(1));
};
