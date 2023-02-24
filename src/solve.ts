(async () => {
  if (process.argv.length !== 3) {
    console.log("Usage: npx ts-node solve.ts <problem>");
    process.exit(1);
  }

  const problem = process.argv[2].padStart(3, "0");
  const { solve } = await import(`./${problem}/p${problem}`);
  console.log(await solve());
})();
