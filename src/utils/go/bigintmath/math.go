package bigintmath

import "math/big"

func Factorial(n int) *big.Int {
	factorial := big.NewInt(1)
	for m := 2; m <= n; m++ {
		factorial.Mul(factorial, big.NewInt(int64(m)))
	}
	return factorial
}
