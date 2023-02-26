const primes = function* () {
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

export const solve = (): string => {
  let count = 0;
  for (const p of primes()) {
    if (++count === 10001) {
      return p.toString();
    }
  }
  throw new Error("No solution found");
};
