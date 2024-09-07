import answers from "../answers.json";

describe("Project Euler", () => {
  test.each(answers.filter(({ problem }) => problem <= 25))(
    "Problem $problem",
    async ({ problem, answer }) => {
      const str = problem.toString().padStart(3, "0");
      const { solve } = await import(`../P${str}/p${str}`);
      expect(await solve()).toBe(answer);
    }
  );
});
