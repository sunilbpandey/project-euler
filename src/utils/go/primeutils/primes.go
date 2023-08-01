package primeutils

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
