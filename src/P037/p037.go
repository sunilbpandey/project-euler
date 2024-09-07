package proble037

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

func isPrime(s string, primes []int) bool {
	return primeutils.IsPrime(strutils.Atoi(s), primes)
}

func isTruncatablePrime(n int, primes []int) bool {
	s := strconv.Itoa(n)
	for i := 0; i < len(s); i++ {
		if !isPrime(s[:len(s)-i], primes) || !isPrime(s[i:], primes) {
			return false
		}
	}
	return true
}

func Solve() string {
	primes := primeutils.GeneratePrimes(1000)
	sum := 0
	for length, count := 0, 0; count < 11; length++ {
		for _, prefix := range []int{2, 3, 5, 7} {
			for middle := range sliceutils.Product([]int{1, 3, 7, 9}, length) {
				for _, suffix := range []int{3, 7} {
					digits := append(append([]int{prefix}, middle...), suffix)
					n := strutils.Atoi(strutils.JoinInts(digits))
					if isTruncatablePrime(n, primes) {
						sum += n
						count += 1
					}
				}
			}
		}
	}
	return strconv.Itoa(sum)
}
