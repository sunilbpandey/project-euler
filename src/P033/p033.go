package problem033

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func Solve() string {
	numerator := 1
	denominator := 1
	for a := 1; a < 10; a++ {
		for b := 1; b < 10; b++ {
			for c := b + 1; c < 10; c++ {
				if 10*a*c == (9*c+a)*b {
					numerator *= 10*a + b
					denominator *= 10*c + a
				}

				if 10*a*b == (9*b+a)*c {
					numerator *= 10*b + a
					denominator *= 10*a + c
				}
			}
		}
	}
	gcd := intutils.Gcd(numerator, denominator)
	return strconv.Itoa(denominator / gcd)
}
