package problem034

import (
	"sort"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
)

func Solve() string {
	factorials := make([]int, 10)
	for d := 0; d < 10; d++ {
		factorials[d] = intutils.Factorial(d)
	}

	answer := 0
	for length := 2; length < 8; length++ {
		for digits := range sliceutils.CombinationsWithReplacement([]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, length) {
			factorialSum := 0
			for _, d := range digits {
				factorialSum += factorials[d]
			}
			factorialSumDigits := intutils.Digits(strconv.Itoa(factorialSum))
			sort.Ints(factorialSumDigits)

			if sliceutils.Equal(digits, factorialSumDigits) {
				answer += factorialSum
			}
		}
	}
	return strconv.Itoa(answer)
}
