export const fibonacci = function* (a = BigInt(1), b = BigInt(1)) {
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
};
