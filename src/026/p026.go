package problem026

import "strconv"

func Solve() string {
	maxCycle := 0
	maxCycleDenominator := 0
	for d := 2; d < 1000; d++ {
		if d%2 == 0 || d%5 == 0 {
			continue
		}

		// Find the smallest k such that 10^k % d = 1
		k := 1
		for power := 10; power%d != 1; power = (power * 10) % d {
			k++
		}

		if k > maxCycle {
			maxCycle = k
			maxCycleDenominator = d
		}
	}
	return strconv.Itoa(maxCycleDenominator)
}
