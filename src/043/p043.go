package problem043

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

func generatePermutations(digits []int) chan []int {
	divisors := []int{1, 1, 1, 2, 3, 5, 7, 11, 13, 17}
	ch := make(chan []int)
	go func() {
		if len(digits) == 10 {
			ch <- digits
		} else {
			for d := 0; d < 10; d++ {
				if sliceutils.Contains(digits, d) {
					continue
				}

				// d1 cannot be 0
				if len(digits) == 0 && d == 0 {
					continue
				}

				// d4 must be even
				if len(digits) == 3 && d%2 != 0 {
					continue
				}

				// d6 must be 0 or 5
				if len(digits) == 5 && d != 0 && d != 5 {
					continue
				}

				divisor := divisors[len(digits)]
				if len(digits) > 2 {
					n := digits[len(digits)-2]*100 + digits[len(digits)-1]*10 + d
					if n%divisor != 0 {
						continue
					}
				}

				for p := range generatePermutations(append(digits, d)) {
					ch <- p
				}
			}
		}
		close(ch)
	}()
	return ch
}

func Solve() string {
	sum := 0
	for perm := range generatePermutations([]int{}) {
		sum += strutils.Atoi(strutils.JoinInts(perm))
	}
	return strconv.Itoa(sum)
}
