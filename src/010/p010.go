package problem010

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/primeutils"
)

func Solve() string {
	primes := primeutils.GeneratePrimes(2000000)
	primeSum := 0
	for _, p := range primes {
		primeSum += p
	}
	return strconv.Itoa(primeSum)
}
