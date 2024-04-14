package problem060

import (
	"math"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/primeutils"
)

var primeCache = make(map[int]bool)
var primes []int

func isPrime(n int) bool {
	if _, exists := primeCache[n]; !exists {
		primeCache[n] = primeutils.IsPrime(n, primes)
	}
	return primeCache[n]
}

func concat(a, b int) int {
	return a*int(math.Pow(10.0, math.Ceil(math.Log10(float64(b))))) + b
}

func isPrimePair(a, b int) bool {
	return isPrime(concat(a, b)) && isPrime(concat(b, a))
}

func findPrimeSetSum(candidates []int) int {
	for i := 0; i < len(candidates)-4; i++ {
		a := candidates[i]
		for j := i + 1; j < len(candidates)-3; j++ {
			b := candidates[j]
			if !isPrimePair(a, b) {
				continue
			}
			for k := j + 1; k < len(candidates)-2; k++ {
				c := candidates[k]
				if !isPrimePair(a, c) || !isPrimePair(b, c) {
					continue
				}
				for l := k + 1; l < len(candidates)-1; l++ {
					d := candidates[l]
					if !isPrimePair(a, d) || !isPrimePair(b, d) || !isPrimePair(c, d) {
						continue
					}
					for _, e := range candidates[l+1:] {
						if isPrimePair(a, e) && isPrimePair(b, e) && isPrimePair(c, e) && isPrimePair(d, e) {
							return a + b + c + d + e
						}
					}
				}
			}
		}
	}
	return math.MaxInt
}

func Solve() string {
	primes = primeutils.GeneratePrimes(10000)

	candidates := []int{3}
	for _, p := range primes[3:] {
		if p%3 == 1 {
			candidates = append(candidates, p)
		}
	}
	sum1 := findPrimeSetSum(candidates)

	candidates = []int{3}
	for _, p := range primes[3:] {
		if p%3 == 2 {
			candidates = append(candidates, p)
		}
	}
	sum2 := findPrimeSetSum(candidates)
	return strconv.Itoa(min(sum1, sum2))
}
