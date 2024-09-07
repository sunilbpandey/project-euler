const isPalindrome = (n: number): boolean => {
  const s = n.toString();
  return s === s.split("").reverse().join("");
};

// Brute force implementation
export const solve1 = (): string => {
  let largestPalindrome = 0;
  for (let i = 100; i < 1000; i++) {
    for (let j = 100; j < 1000; j++) {
      const n = i * j;
      if (isPalindrome(n) && n > largestPalindrome) {
        largestPalindrome = n;
      }
    }
  }
  return largestPalindrome.toString();
};

// More efficient implementation
export const solve2 = (): string => {
  let largestPalindrome = 0;
  for (let i = 901; i < 1000; i += 2) {
    if (i % 5 === 0) continue;

    for (let j = 949; j < 1000; j += 2) {
      if (j % 5 === 0) continue;

      const n = i * j;
      if (isPalindrome(n) && n > largestPalindrome) {
        largestPalindrome = n;
      }
    }
  }
  return largestPalindrome.toString();
};

export const solve = (): string => {
  let largestPalindrome = 0;

  for (let b = 0; b < 10; b++) {
    for (let c = 0; c < 10; c++) {
      const n = 10010 * b + 1100 * c + 900009;
      for (let d = 949; d < 1000; d += 2) {
        if (d % 5 === 0) continue;
        if (n > largestPalindrome && n % d === 0) {
          const m = n / d;
          if (m >= 100 && m < 1000) {
            largestPalindrome = n;
          }
        }
      }
    }
  }
  return largestPalindrome.toString();
};
