package problem046

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
)

func isSumOfPrimeAndTwiceASquare(n int, primes []int, doubleSquares []int) bool {
	for _, dsq := range doubleSquares {
		if dsq > n {
			break
		}

		if primeutils.IsPrime(n-dsq, primes) {
			return true
		}
	}
	return false
}

func Solve() string {
	primes := primeutils.GeneratePrimes(1000)
	doubleSquares := make([]int, 1000)
	for i := 0; i < 1000; i++ {
		doubleSquares[i] = 2 * i * i
	}

	answer := 0
	for n := 9; n < 1000000; n += 2 {
		if !primeutils.IsPrime(n, primes) && !isSumOfPrimeAndTwiceASquare(n, primes, doubleSquares) {
			answer = n
			break
		}
	}
	return strconv.Itoa(answer)
}
