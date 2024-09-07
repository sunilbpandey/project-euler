package problem040

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func getChampernowneDigit(index int) int {
	pow := 1
	for i := 1; ; i++ {
		nextGroup := i * 9 * pow
		if index < nextGroup {
			number := pow + (index-1)/i
			digit := (index-1)%i + 1
			return number / intutils.Pow(10, i-digit) % 10
		}
		index -= nextGroup
		pow *= 10
	}
}

func Solve() string {
	product := 1
	for i := 1; i <= 1000000; i *= 10 {
		product *= getChampernowneDigit(i)
	}
	return strconv.Itoa(product)
}
