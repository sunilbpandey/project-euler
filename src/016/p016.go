package problem016

import (
	"math/big"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/bigintmath"
)

func Solve() string {
	n := big.NewInt(0).Exp(big.NewInt(2), big.NewInt(1000), nil)
	sum := bigintmath.DigitSum(n)
	return strconv.Itoa(sum)
}
