package problem010

import "strconv"

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

func Solve() string {
	primes := GeneratePrimes(2000000)
	primeSum := 0
	for _, p := range primes {
		primeSum += p
	}
	return strconv.Itoa(primeSum)
}
