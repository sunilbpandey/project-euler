package problem057

import (
	"math/big"
	"strconv"
)

func Solve() string {
	count := 0
	n, d := big.NewInt(1), big.NewInt(1)
	for i := 1; i < 1000; i++ {
		n.Add(n, d).Add(n, d)
		d.Sub(n, d)
		if len(n.String()) > len(d.String()) {
			count++
		}
	}
	return strconv.Itoa(count)
}
