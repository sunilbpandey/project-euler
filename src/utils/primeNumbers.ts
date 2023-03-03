export const primes = function* () {
  const primes = [2];
  yield 2;

  for (let n = 3; ; n += 2) {
    let isPrime = true;
    const limit = Math.sqrt(n);
    for (const p of primes) {
      if (p > limit) {
        break;
      }

      if (n % p === 0) {
        isPrime = false;
        break;
      }
    }

    if (isPrime) {
      yield n;
      primes.push(n);
    }
  }
};

const divide = (n: number, d: number) => {
  let exponent = 0;
  while (n % d === 0) {
    n /= d;
    exponent++;
  }
  return { remainder: n, exponent };
};

export const factorize = (n: number) => {
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
