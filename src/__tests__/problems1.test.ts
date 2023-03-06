import { solutions } from "./solutions";
import { solve } from "./utils";

describe("Project Euler", () => {
  test.each(solutions.filter(({ problem }) => problem > 10 && problem <= 20))(
    "Problem $problem",
    async ({ problem, solution }) => {
      expect(await solve(problem)).toBe(solution);
    }
  );
});
