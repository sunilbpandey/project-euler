package problem052

import (
	"sort"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
)

func Solve() string {
	pow := 2
	for ; ; pow++ {
		limit := intutils.Pow(10, pow+1)
		start := intutils.Pow(10, pow)
		for n := start; 6*n < limit; n++ {
			if n%3 != 0 {
				continue
			}

			nDigits := intutils.Digits(n)
			digitCounts := make([]int, 10)
			for _, d := range nDigits {
				digitCounts[d]++
			}

			if (digitCounts[0] == 0 && digitCounts[5] == 0) ||
				(digitCounts[2] == 0 && digitCounts[3] == 0) ||
				(digitCounts[3] == 0 && digitCounts[4] == 0) ||
				(digitCounts[4] == 0 && digitCounts[5] == 0) ||
				(digitCounts[5] == 0 && digitCounts[6] == 0) ||
				(digitCounts[6] == 0 && digitCounts[7] == 0) {
				continue
			}

			sort.Ints(nDigits)
			sameDigits := true
			for i := 2; i <= 6 && sameDigits; i++ {
				mDigits := intutils.Digits(i * n)
				sort.Ints(mDigits)
				sameDigits = sliceutils.Equal(mDigits, nDigits)
			}
			if sameDigits {
				return strconv.Itoa(n)
			}
		}
	}
}
