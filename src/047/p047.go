package problem047

import "strconv"

func Solve() string {
	sieve := make(map[int][]int)

	// Count of numbers with 4 prime factors left to find
	remaining := 4

	for n := 2; ; n++ {
		factors := []int{n}
		if _, found := sieve[n]; found {
			// n is composite and sieve[n] contains its prime factors
			factors = sieve[n]
		}

		if len(factors) == 4 {
			remaining--
			if remaining == 0 {
				return strconv.Itoa(n - 3)
			}
		} else {
			// Either n is prime or doesn't have exactly 4 prime factors
			// Reset the count to 4
			remaining = 4
		}

		// Mark next multiple of each factor
		for _, f := range factors {
			sieve[n+f] = append(sieve[n+f], f)
		}
	}
}
