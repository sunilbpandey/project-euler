package problem045

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math"
	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func isHexagonal(n int) bool {
	sqrt := intutils.Sqrt(8*n + 1)
	return sqrt*sqrt == 8*n+1 && sqrt%4 == 3
}

func Solve() string {
	p := 0
	for p = range math.PentagonalNumbers() {
		if p > 40755 && isHexagonal(p) {
			break
		}
	}
	return strconv.Itoa(p)
}
