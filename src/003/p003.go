package problem003

import (
	"math"
	"strconv"
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

	sqrt := int(math.Sqrt(float64(n)))
	for d := 3; d <= sqrt; d += 2 {
		if n%d == 0 {
			largestFactor = d
			n = divide(n, d)
		}
	}
	return strconv.Itoa(largestFactor)
}
