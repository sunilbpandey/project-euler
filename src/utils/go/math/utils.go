package math

import (
	"sort"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func IsPandigital(n string) bool {
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
