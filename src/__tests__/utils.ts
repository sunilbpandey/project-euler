export const solve = async (problem: number): Promise<string> => {
  const str = problem.toString().padStart(3, "0");
  const { solve } = await import(`../${str}/p${str}`);
  return solve();
};
