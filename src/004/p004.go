package problem004

import (
	"strconv"
)

func Solve() string {
	largestPalindrome := 0
	for b := 0; b < 10; b++ {
		for c := 0; c < 10; c++ {
			n := 10010*b + 1100*c + 900009
			for d := 949; d < 1000; d += 2 {
				if n > largestPalindrome && n%d == 0 {
					if m := n / d; m > 99 && m < 1000 {
						largestPalindrome = n
					}
				}
			}
		}
	}
	return strconv.Itoa(largestPalindrome)
}
