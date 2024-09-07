import { factorial } from "../utils";

let count = 0;

const permutations = (digits: number[], current: number[]): string => {
  if (digits.length === 1) {
    count++;
    if (count === 1000000) {
      return [...current, ...digits].join("");
    }
    return "";
  }

  for (let i = 0; i < digits.length; i++) {
    const next = [...current, digits[i]];
    const result = permutations(
      [...digits.slice(0, i), ...digits.slice(i + 1)],
      next
    );
    if (result) {
      return result;
    }
  }
  return "";
};

const solve1 = (): string => {
  return permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], []);
};

const findLeadingDigit = (digits: number[], permutationIndex: number) => {
  const fac = Number(factorial(digits.length - 1));
  const i = Math.floor(permutationIndex / fac);
  return { digit: digits[i], remainder: permutationIndex % fac };
};

export const solve = (): string => {
  const result: number[] = [];

  const digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  let index = 999999;
  while (digits.length > 0) {
    const { digit, remainder } = findLeadingDigit(digits, index);
    result.push(digit);
    digits.splice(digits.indexOf(digit), 1);
    index = remainder;
  }

  return result.join("");
};
