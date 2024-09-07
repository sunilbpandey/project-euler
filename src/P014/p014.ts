const getCollatzSequenceLength = (
  start: number,
  chainLengths: Record<number, number>
): number => {
  let n = start;
  let len = 0;
  while (chainLengths[n] === undefined) {
    len++;
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
  }
  chainLengths[start] = len + chainLengths[n];
  return chainLengths[start];
};

export const solve = (): string => {
  const chainLengths: Record<number, number> = {};
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
