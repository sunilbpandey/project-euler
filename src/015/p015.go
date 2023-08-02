package problem015

import (
	"math/big"

	"github.com/sunilbpandey/project-euler/src/utils/go/bigintmath"
)

func Solve() string {
	fac20 := bigintmath.Factorial(20)
	fac40 := bigintmath.Factorial(40)

	fac20Squared := new(big.Int).Mul(fac20, fac20)
	answer := new(big.Int).Div(fac40, fac20Squared)
	return answer.String()
}
