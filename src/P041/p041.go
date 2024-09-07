package problem041

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

func Solve() string {
	primes := primeutils.GeneratePrimes(2800)
	digits := []int{1, 2, 3, 4, 5, 6, 7}
	max := 0
	for perm := range sliceutils.Permutations(digits, len(digits)) {
		n := strutils.Atoi(strutils.JoinInts(perm))
		if primeutils.IsPrime(n, primes) && n > max {
			max = n
		}
	}
	return strconv.Itoa(max)
}
