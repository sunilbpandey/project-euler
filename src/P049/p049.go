package problem049

import (
	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

func Solve() string {
	answer := ""
	primes := primeutils.GeneratePrimes(10000)
	for _, p := range primes {
		if p < 1000 || p == 1487 {
			continue
		}

		permutations := make(map[int]bool)
		for perm := range sliceutils.Permutations(intutils.Digits(p), 4) {
			r := strutils.Atoi(strutils.JoinInts(perm))
			if r > p && primeutils.IsPrime(r, primes) {
				q := (r + p) / 2
				if _, found := permutations[q]; found {
					answer = strutils.JoinInts([]int{p, q, r})
					break
				}
				permutations[r] = true
			}
		}

		if answer != "" {
			break
		}
	}
	return answer
}
