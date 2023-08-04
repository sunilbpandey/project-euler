package problem021

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func isAmicable(n int) bool {
	m := intutils.SumOfProperDivisors(n)
	return m != n && intutils.SumOfProperDivisors(m) == n
}

func Solve() string {
	sum := 0
	for n := 2; n < 10000; n++ {
		if isAmicable(n) {
			sum += n
		}
	}
	return strconv.Itoa(sum)
}
