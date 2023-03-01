// Return the day of the week of the given day using Zeller's congruence
const weekday = (day: number, month: number, year: number): number => {
  if (month < 3) {
    month += 12;
    year--;
  }

  const century = Math.floor(year / 100);
  year %= 100;

  const dayOfWeek =
    (day +
      Math.floor(2.6 * (month + 1)) +
      year +
      Math.floor(year / 4) +
      Math.floor(century / 4) -
      2 * century) %
    7;
  return dayOfWeek < 0 ? dayOfWeek + 7 : dayOfWeek;
};

export const solve = (): string => {
  let sundays = 0;
  for (let year = 1901; year < 2001; year++) {
    for (let month = 1; month < 13; month++) {
      if (weekday(1, month, year) === 1) {
        sundays++;
      }
    }
  }
  return sundays.toString();
};
