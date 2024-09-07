package problem012

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
)

func Solve() string {
	primes := primeutils.GeneratePrimes(120)
	answer := 0
	for k := 1; ; k++ {
		count1 := primeutils.CountOfDivisors(k, primes)
		count2 := primeutils.CountOfDivisors(2*k-1, primes)
		if count1*count2 > 500 {
			answer = k * (2*k - 1)
			break
		}

		count2 = primeutils.CountOfDivisors(2*k+1, primes)
		if count1*count2 > 500 {
			answer = k * (2*k + 1)
			break
		}
	}
	return strconv.Itoa(answer)
}
