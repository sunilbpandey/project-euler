package problem020

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/bigintutils"
)

func Solve() string {
	return strconv.Itoa(bigintutils.DigitSum(bigintutils.Factorial(100)))
}
