package problem058

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
)

func Solve() string {
	primes := primeutils.GeneratePrimes(30000)
	last := 1
	countNumbers := 1 // 1 is already counted
	countPrimes := 0
	for side := 3; ; side += 2 {
		for i := 0; i < 3; i++ {
			last += side - 1
			if primeutils.IsPrime(last, primes) {
				countPrimes++
			}
		}
		countNumbers += 4
		if countPrimes*10 < countNumbers {
			return strconv.Itoa(side)
		}
		last += side - 1
	}
}
