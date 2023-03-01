const solutions = [
  { problem: 1, solution: "233168" },
  { problem: 2, solution: "4613732" },
  { problem: 3, solution: "6857" },
  { problem: 4, solution: "906609" },
  { problem: 5, solution: "232792560" },
  { problem: 6, solution: "25164150" },
  { problem: 7, solution: "104743" },
  { problem: 8, solution: "23514624000" },
  { problem: 9, solution: "31875000" },
  { problem: 10, solution: "142913828922" },
  { problem: 11, solution: "70600674" },
  { problem: 12, solution: "76576500" },
  { problem: 13, solution: "5537376230" },
  { problem: 14, solution: "837799" },
  { problem: 15, solution: "137846528820" },
  { problem: 16, solution: "1366" },
];

describe("Project Euler", () => {
  test.each(solutions)("Problem $problem", async ({ problem, solution }) => {
    const str = problem.toString().padStart(3, "0");
    const { solve } = await import(`../${str}/p${str}`);
    const result = solve();
    expect(result).toBe(solution);
  });
});
