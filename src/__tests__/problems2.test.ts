import { solutions } from "./solutions";
import { solve } from "./utils";

describe("Project Euler", () => {
  test.each(solutions.filter(({ problem }) => problem > 20 && problem <= 30))(
    "Problem $problem",
    async ({ problem, solution }) => {
      expect(await solve(problem)).toBe(solution);
    }
  );
});
