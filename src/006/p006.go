package problem006

import (
	"math"
	"strconv"
)

func IntPow(x int, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func Solve() string {
	n := 100
	sumOfSquares := n * (n + 1) * (2*n + 1) / 6
	squareOfSum := IntPow(n*(n+1)/2, 2)
	return strconv.Itoa(squareOfSum - sumOfSquares)
}
