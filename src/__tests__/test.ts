const solutions = [
  { problem: 1, solution: "233168" },
  { problem: 2, solution: "4613732" },
  { problem: 3, solution: "6857" },
  { problem: 4, solution: "906609" },
  { problem: 5, solution: "232792560" },
];

describe("Project Euler", () => {
  test.each(solutions)("Problem $problem", async ({ problem, solution }) => {
    const str = problem.toString().padStart(3, "0");
    const { solve } = await import(`../${str}/p${str}`);
    const result = solve();
    expect(result).toBe(solution);
  });
});
