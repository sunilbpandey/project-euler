package problem006

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/intmath"
)

func Solve() string {
	n := 100
	sumOfSquares := n * (n + 1) * (2*n + 1) / 6
	squareOfSum := intmath.Pow(n*(n+1)/2, 2)
	return strconv.Itoa(squareOfSum - sumOfSquares)
}
