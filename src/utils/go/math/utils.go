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

func figurateNumbers(step int) chan int {
	ch := make(chan int)
	go func() {
		for diff, n := 1, 0; ; diff += step {
			n += diff
			ch <- n
		}
	}()
	return ch
}

func PentagonalNumbers() chan int {
	return figurateNumbers(3)
}
