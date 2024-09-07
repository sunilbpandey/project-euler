package problem035

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

func isCircularPrime(digits []int, primes []int) bool {
	str := strutils.JoinInts(digits)
	for i := 0; i < len(digits); i++ {
		if !primeutils.IsPrime(strutils.Atoi(str), primes) {
			return false
		}
		str = str[1:] + str[:1]
	}
	return true
}

func Solve() string {
	primes := primeutils.GeneratePrimes(1000)

	// We are given that 13 circular primes exist below 100
	count := 13

	for length := 3; length < 7; length++ {
		for digits := range sliceutils.Product([]int{1, 3, 7, 9}, length) {
			if isCircularPrime(digits, primes) {
				count++
			}
		}
	}
	return strconv.Itoa(count)
}
