export const range = (start: number, stop?: number): number[] => {
  if (stop === undefined) {
    // If only start is given, start at 0 and treat the given number as stop instead
    [start, stop] = [0, start];
  }
  return Array.from({ length: stop - start }, (_, i) => i + start);
};
