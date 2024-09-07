package problem038

import (
	"fmt"

	"github.com/sunilbpandey/project-euler/src/utils/go/math"
)

func Solve() string {
	answer := "123456789"
	for m := 9182; m < 10000; m++ {
		n := m * 2
		str := fmt.Sprintf("%d%d", m, n)
		if math.IsPandigital(str) {
			if str > answer {
				answer = str
			}
		}
	}
	return answer
}
