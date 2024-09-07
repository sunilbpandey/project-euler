package problem029

import (
	"math/big"
	"strconv"
)

func Solve() string {
	terms := make(map[string]bool)
	for a := 2; a <= 100; a++ {
		for b := 2; b <= 100; b++ {
			n := big.NewInt(0).Exp(big.NewInt(int64(a)), big.NewInt(int64(b)), nil)
			terms[n.String()] = true
		}
	}
	return strconv.Itoa(len(terms))
}
