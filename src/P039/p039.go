package problem039

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func Solve() string {
	solutions := make([]int, 1001)
	maxSolutions := 0
	maxP := 0
	for m := 2; m < 22; m++ {
		for n := 1; n < m; n++ {
			if intutils.Gcd(m, n) != 1 || (m-n)%2 == 0 {
				continue
			}

			pp := 2 * m * (m + n)
			for k := 1; ; k++ {
				p := k * pp
				if p > 1000 {
					break
				}

				solutions[p]++
				if solutions[p] > maxSolutions {
					maxSolutions = solutions[p]
					maxP = p
				}
			}
		}
	}
	return strconv.Itoa(maxP)
}
