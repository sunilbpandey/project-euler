package problem007

import "strconv"

func Solve() string {
	primes := []int{2}
	for n := 3; len(primes) < 10001; n += 2 {
		isPrime := true
		for _, p := range primes {
			if n%p == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			primes = append(primes, n)
		}
	}
	return strconv.Itoa(primes[len(primes)-1])
}
