package problem005

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func Solve() string {
	lcm := 1
	for n := 2; n <= 20; n++ {
		lcm = intutils.Lcm(lcm, n)
	}
	return strconv.Itoa(lcm)
}
