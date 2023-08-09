package bigintutils

import (
	"math/big"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func DigitSum(n *big.Int) int {
	sum := 0
	for _, digit := range intutils.Digits(n.String()) {
		sum += digit
	}
	return sum
}

func Factorial(n int) *big.Int {
	factorial := big.NewInt(1)
	for m := 2; m <= n; m++ {
		factorial.Mul(factorial, big.NewInt(int64(m)))
	}
	return factorial
}
