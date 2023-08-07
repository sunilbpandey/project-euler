package problem030

import "strconv"

func Solve() string {
	digits := make([]int, 10)
	fifthPowers := make(map[int]int)
	for d := 0; d < 10; d++ {
		digits[d] = d
		fifthPowers[d] = d * d * d * d * d
	}

	answer := 0
	for _, a := range digits {
		for _, b := range digits {
			for _, c := range digits {
				for _, d := range digits {
					for _, e := range digits {
						for _, f := range digits {
							n := a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
							if n == 1 {
								continue
							}

							digitPowerSum := fifthPowers[a] + fifthPowers[b] + fifthPowers[c] + fifthPowers[d] + fifthPowers[e] + fifthPowers[f]
							if digitPowerSum == n {
								answer += digitPowerSum
							}
						}
					}
				}
			}
		}
	}
	return strconv.Itoa(answer)
}
