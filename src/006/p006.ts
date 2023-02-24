// Brute force implementation
export const solve1 = (): string => {
  const n = 100;
  let sumOfSquares = 0;
  let squareOfSum = 0;
  for (let i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    squareOfSum += i;
  }

  squareOfSum *= squareOfSum;
  return (squareOfSum - sumOfSquares).toString();
};

// Direct computation
export const solve = (): string => {
  const n = 100;
  const sumOfSquares = (n * (n + 1) * (2 * n + 1)) / 6;
  const squareOfSum = ((n * (n + 1)) / 2) ** 2;
  return (squareOfSum - sumOfSquares).toString();
};
