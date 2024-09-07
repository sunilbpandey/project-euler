package problem023

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func isAbundantSum(n int, isAbundant []bool) bool {
	for i := 1; i <= n/2; i++ {
		if isAbundant[i] && isAbundant[n-i] {
			return true
		}
	}
	return false
}

func Solve() string {
	nonAbundantSum := 0
	isAbundant := make([]bool, 28124)
	for n := 1; n <= 28123; n++ {
		if intutils.SumOfProperDivisors(n) > n {
			isAbundant[n] = true
		}

		if !isAbundantSum(n, isAbundant) {
			nonAbundantSum += n
		}
	}
	return strconv.Itoa(nonAbundantSum)
}
