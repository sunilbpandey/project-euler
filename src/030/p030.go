package problem030

import (
	"sort"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
)

func Solve() string {
	fifthPowers := make([]int, 10)
	for d := 0; d < 10; d++ {
		fifthPowers[d] = d * d * d * d * d
	}

	answer := 0
	for length := 2; length < 8; length++ {
		for _, digits := range sliceutils.CombinationsWithReplacement([]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, length) {
			powerSum := 0
			for _, d := range digits {
				powerSum += fifthPowers[d]
			}
			powerSumDigits := intutils.Digits(strconv.Itoa(powerSum))
			sort.Ints(powerSumDigits)

			if sliceutils.Equal(digits, powerSumDigits) {
				answer += powerSum
			}
		}
	}
	return strconv.Itoa(answer)
}
