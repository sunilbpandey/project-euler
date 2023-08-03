package problem015

import (
	"math/big"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/bigintutils"
)

func Solve() string {
	fac20 := bigintutils.Factorial(20)
	fac40 := bigintutils.Factorial(40)

	fac20Squared := new(big.Int).Mul(fac20, fac20)
	answer := new(big.Int).Div(fac40, fac20Squared)
	return answer.String()
}
