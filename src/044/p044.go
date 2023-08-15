package problem044

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/math"
)

func Solve() string {
	pentagonals := make(map[int]bool)
	answer := 0
	for p := range math.PentagonalNumbers() {
		for q := range pentagonals {
			if _, found := pentagonals[p-q]; !found {
				continue
			}

			if _, found := pentagonals[p-2*q]; !found {
				continue
			}
			answer = p - 2*q
			break
		}
		if answer > 0 {
			break
		}
		pentagonals[p] = true
	}
	return strconv.Itoa(answer)
}
