import answers from "../answers.json";
import { solve } from "./utils";

describe("Project Euler", () => {
  test.each(answers.filter(({ problem }) => problem > 20 && problem <= 30))(
    "Problem $problem",
    async ({ problem, answer }) => {
      expect(await solve(problem)).toBe(answer);
    }
  );
});
