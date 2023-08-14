package problem032

import (
	"fmt"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math"
)

func Solve() string {
	products := make(map[int]bool)
	sum := 0
	for m := 1; m < 100; m++ {
		for n := 1000 / m; n < 10000/m; n++ {
			p := m * n
			if math.IsPandigital(fmt.Sprintf("%d%d%d", m, n, p)) {
				if _, found := products[p]; !found {
					products[p] = true
					sum += p
				}
			}
		}
	}
	return strconv.Itoa(sum)
}
