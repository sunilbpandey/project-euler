package problem056

import (
	"math/big"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/bigintutils"
)

func Solve() string {
	maxDigitSum := 0
	for a := 90; a < 100; a++ {
		for b := 90; b < 100; b++ {
			exp := big.NewInt(0).Exp(big.NewInt(int64(a)), big.NewInt(int64(b)), nil)
			digitSum := bigintutils.DigitSum(exp)
			if digitSum > maxDigitSum {
				maxDigitSum = digitSum
			}
		}
	}
	return strconv.Itoa(maxDigitSum)
}
