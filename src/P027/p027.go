package problem027

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
)

func Solve() string {
	primes := primeutils.GeneratePrimes(1415)

	maxSoFar := 0
	product := 0
	for a := -999; a < 1000; a += 2 {
		for _, b := range primes {
			if b > 1000 {
				break
			}

			for n := 0; n < b; n++ {
				number := n*n + a*n + b
				if !primeutils.IsPrime(number, primes) {
					if n > maxSoFar {
						maxSoFar = n
						product = a * b
					}
					break
				}
			}
		}
	}
	return strconv.Itoa(product)
}
