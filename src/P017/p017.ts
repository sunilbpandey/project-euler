const numberNames: Record<number, string> = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
};

const getNumberName = (number: number): string => {
  if (numberNames[number]) {
    return numberNames[number];
  }

  if (number < 100) {
    const units = number % 10;
    let name = numberNames[number - units];
    return `${name}${units > 0 ? numberNames[units] : ""}`;
  }

  if (number < 1000) {
    const tens = number % 100;
    let name = `${numberNames[Math.floor(number / 100)]}hundred`;
    return `${name}${tens > 0 ? `and${getNumberName(tens)}` : ""}`;
  }
  return "onethousand";
};

export const solve = (): string => {
  let letterCount = 0;
  for (let i = 1; i <= 1000; i++) {
    const name = getNumberName(i);
    letterCount += name.length;
  }
  return letterCount.toString();
};
