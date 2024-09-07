package problem028

import "strconv"

func Solve() string {
	sum := 1
	for n := 1; n < 501; n++ {
		sum += 4 * (4*n*n + n + 1)
	}
	return strconv.Itoa(sum)
}
