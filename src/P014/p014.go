package problem014

import "strconv"

func Solve() string {
	var chainLengths [1000000]int
	chainLengths[1] = 1

	maxChainLength := 0
	maxChainLengthStart := 0

	for start := 2; start < 1000000; start++ {
		n := start
		length := 0
		for n >= start {
			length++
			if n%2 == 0 {
				n /= 2
			} else {
				n = 3*n + 1
			}
		}
		chainLengths[start] = length + chainLengths[n]
		if chainLengths[start] > maxChainLength {
			maxChainLength = chainLengths[start]
			maxChainLengthStart = start
		}
	}
	return strconv.Itoa(maxChainLengthStart)
}
