package problem003

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func divide(number int, divisor int) int {
	for number%divisor == 0 {
		number /= divisor
	}
	return number
}

func Solve() string {
	n := 600851475143
	largestFactor := 1

	if n%2 == 0 {
		largestFactor = 2
		n = divide(n, 2)
	}

	sqrt := intutils.Sqrt(n)
	for d := 3; d <= sqrt; d += 2 {
		if n%d == 0 {
			largestFactor = d
			n = divide(n, d)
		}
	}
	return strconv.Itoa(largestFactor)
}
