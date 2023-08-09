package problem032

import (
	"fmt"
	"sort"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func isPandigital(n string) bool {
	digits := intutils.Digits(n)
	if len(digits) != 9 {
		return false
	}

	sort.Ints(digits)
	for i := 0; i < 9; i++ {
		if digits[i] != i+1 {
			return false
		}
	}
	return true
}

func Solve() string {
	products := make(map[int]bool)
	sum := 0
	for m := 1; m < 100; m++ {
		for n := 1000 / m; n < 10000/m; n++ {
			p := m * n
			if isPandigital(fmt.Sprintf("%d%d%d", m, n, p)) {
				if _, found := products[p]; !found {
					products[p] = true
					sum += p
				}
			}
		}
	}
	return strconv.Itoa(sum)
}
