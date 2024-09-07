package problem001

import "strconv"

func Solve() string {
	answer := 0
	for n := 1; n < 1000; n++ {
		if n%3 == 0 || n%5 == 0 {
			answer += n
		}
	}
	return strconv.Itoa(answer)
}
