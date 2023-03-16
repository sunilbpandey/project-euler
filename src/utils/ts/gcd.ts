export const gcd = (a: number, b: number): number => {
  while (a !== b) {
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
  return a;
};
