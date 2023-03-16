import { range } from "../range";

describe("Range", () => {
  test.each([
    { start: 5, expected: [0, 1, 2, 3, 4] },
    { start: 0, expected: [] },
    { start: -1, expected: [] },
  ])(
    "Range with start as $start and no stop should be $expected",
    ({ start, expected }) => {
      expect(range(start)).toEqual(expected);
    }
  );

  test.each([
    { start: 5, stop: 10, expected: [5, 6, 7, 8, 9] },
    { start: 0, stop: 5, expected: [0, 1, 2, 3, 4] },
    { start: 0, stop: 0, expected: [] },
    { start: 5, stop: 0, expected: [] },
    { start: 0, stop: -5, expected: [] },
    { start: -1, stop: 2, expected: [-1, 0, 1] },
    { start: -10, stop: -5, expected: [-10, -9, -8, -7, -6] },
  ])(
    "Range from $start to $stop should be $expected",
    ({ start, stop, expected }) => {
      expect(range(start, stop)).toEqual(expected);
    }
  );
});
