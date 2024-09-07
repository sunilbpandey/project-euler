package problem055

import (
	"math/big"
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

func reverse(n *big.Int) *big.Int {
	r, _ := big.NewInt(0).SetString(strutils.Reverse(n.String()), 10)
	return r
}

func isLychrel(num int) bool {
	n := big.NewInt(int64(num))
	for i := 0; i < 50; i++ {
		n.Add(n, reverse(n))
		if strutils.IsPalindrome(n.String()) {
			return false
		}
	}
	return true
}

func Solve() string {
	count := 0
	for n := 1; n < 10000; n++ {
		if isLychrel(n) {
			count++
		}
	}
	return strconv.Itoa(count)
}
