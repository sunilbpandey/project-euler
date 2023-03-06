import { readFileSync } from "fs";
import * as path from "path";

const getNameValue = (name: string): number => {
  let value = 0;
  for (let i = 0; i < name.length; i++) {
    value += name.charCodeAt(i) - "A".charCodeAt(0) + 1;
  }
  return value;
};

export const solve = (): string => {
  const contents = readFileSync(
    path.resolve(__dirname, "./p022_names.txt"),
    "utf8"
  );
  const names = contents.split(",");
  names.sort();

  let score = 0;
  names.forEach((name, index) => {
    name = name.replace(/^"(.+)"$/g, "$1");
    score += getNameValue(name) * (index + 1);
  });
  return score.toString();
};
