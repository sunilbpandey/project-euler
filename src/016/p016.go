package problem016

import (
	"math/big"
	"strconv"
)

func Solve() string {
	n := big.NewInt(0).Exp(big.NewInt(2), big.NewInt(1000), nil)
	sum := 0
	for _, digit := range n.String() {
		sum += int(digit - '0')
	}
	return strconv.Itoa(sum)
}
