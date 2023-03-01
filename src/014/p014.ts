const getCollatzSequenceLength = (
  n: number,
  chainLengths: { [key: number]: number }
): number => {
  if (chainLengths[n] === undefined) {
    const next = n % 2 === 0 ? n / 2 : 3 * n + 1;
    chainLengths[n] = getCollatzSequenceLength(next, chainLengths) + 1;
  }
  return chainLengths[n];
};

export const solve = (): string => {
  const chainLengths: { [key: number]: number } = {};
  chainLengths[1] = 1;

  let maxChainLength = 0;
  let maxChainLengthStart = 0;
  for (let i = 1; i < 1000000; i++) {
    const len = getCollatzSequenceLength(i, chainLengths);
    if (len > maxChainLength) {
      maxChainLength = len;
      maxChainLengthStart = i;
    }
  }
  return maxChainLengthStart.toString();
};
