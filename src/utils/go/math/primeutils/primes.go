package primeutils

import "github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"

func CountOfDivisors(n int, primes []int) int {
	factors := Factorize(n, primes)
	divisorCount := 1
	for _, exponent := range factors {
		divisorCount *= exponent + 1
	}
	return divisorCount
}

func Factorize(n int, primes []int) map[int]int {
	limit := intutils.Sqrt(n)
	factors := make(map[int]int)
	for _, p := range primes {
		if n == 1 || p > limit {
			break
		}

		exponent := 0
		for n%p == 0 {
			exponent++
			n /= p
		}

		if exponent > 0 {
			factors[p] = exponent
		}
	}

	if n > 1 {
		factors[n] = 1
	}
	return factors
}

func GeneratePrimes(limit int) []int {
	primes := []int{2}
	sieve := make([]bool, limit)
	for n := 3; n < limit; n += 2 {
		if !sieve[n] {
			primes = append(primes, n)
			for m := n * n; m < limit; m += n {
				sieve[m] = true
			}
		}
	}
	return primes
}
