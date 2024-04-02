package problem050

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
)

func Solve() string {
	primes := primeutils.GeneratePrimes(4000)

	maxTermCount := 21
	maxTermPrime := 953
	for i := range primes {
		total := primes[i]
		for j := i + 1; j < len(primes); j++ {
			total += primes[j]
			if total > 1000*1000 {
				break
			}

			if j-i+1 > maxTermCount && primeutils.IsPrime(total, primes) {
				maxTermCount = j - i + 1
				maxTermPrime = total
			}
		}
	}
	return strconv.Itoa(maxTermPrime)
}
