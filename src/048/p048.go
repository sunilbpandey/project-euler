package problem048

import "strconv"

func Solve() string {
	total := 0
	for n := 1; n <= 1000; n++ {
		power := 1
		for i := 1; i <= n; i++ {
			power = (power * n) % 10000000000
		}
		total = (total + power) % 10000000000
	}
	return strconv.Itoa(total)
}
