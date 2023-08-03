package bigintmath

import "math/big"

func DigitSum(n *big.Int) int {
	sum := 0
	for _, digit := range n.String() {
		sum += int(digit - '0')
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
