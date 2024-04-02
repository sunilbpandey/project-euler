package problem051

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

var digits = []string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}

func generatePrimeFamily(n int, primes []int) []int {
	str := strconv.Itoa(n)
	for i := 0; i < len(str)-1; i++ {
		for j := i + 1; j < len(str)-1; j++ {
			for k := j + 1; k < len(str)-1; k++ {
				if str[i] == str[j] && str[j] == str[k] {
					family := []int{}
					for _, d := range digits {
						candidate := str[:i] + d + str[i+1:j] + d + str[j+1:k] + d + str[k+1:]
						if p := strutils.Atoi(candidate); primeutils.IsPrime(p, primes) {
							family = append(family, p)
						}
					}
					if len(family) == 8 {
						return family
					}
				}
			}
		}
	}
	return nil
}

func Solve() string {
	sieve := make(map[int][]int)
	primes := []int{}

	for n := 2; ; n++ {
		var factors []int
		if _, exists := sieve[n]; exists {
			factors = sieve[n]
			delete(sieve, n)
		} else {
			factors = []int{n}
			primes = append(primes, n)
			if family := generatePrimeFamily(n, primes); family != nil {
				return strconv.Itoa(n)
			}
		}

		for _, f := range factors {
			sieve[n+f] = append(sieve[n+f], f)
		}
	}
}
