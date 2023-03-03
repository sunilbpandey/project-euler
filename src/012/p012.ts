const divide = (n: number, d: number) => {
  let exponent = 0;
  while (n % d === 0) {
    n /= d;
    exponent++;
  }
  return { remainder: n, exponent };
};

const factorize = (n: number) => {
  const factors: Record<number, number> = {};

  const factorizeInternal = (d: number) => {
    const { remainder, exponent } = divide(n, d);
    if (exponent > 0) {
      factors[d] = exponent;
      n = remainder;
    }
  };

  factorizeInternal(2);

  // Ideally, we should generate prime numbers, but just testing all odd numbers is fast enough
  const sqrt = Math.sqrt(n);
  for (let d = 3; n > 1 && d <= sqrt; d += 2) {
    factorizeInternal(d);
  }

  if (n > 1) {
    factors[n] = 1;
  }
  return factors;
};

const divisorCount = (n: number) => {
  return Object.values(factorize(n))
    .map((power) => power + 1)
    .reduce((prev, cur) => prev * cur, 1);
};

const triangleNumbers = function* () {
  for (let t = 0, n = 1; ; n++) {
    t += n;
    yield t;
  }
};

export const solve = (): string => {
  for (const t of triangleNumbers()) {
    if (divisorCount(t) > 500) {
      return t.toString();
    }
  }
  throw new Error("No solution found");
};
