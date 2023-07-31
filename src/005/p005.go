package problem005

import "strconv"

func Gcd(a int, b int) int {
	for a != b {
		if a > b {
			a -= b
		} else {
			b -= a
		}
	}
	return a
}

func Lcm(a int, b int) int {
	return a * b / Gcd(a, b)
}

func Solve() string {
	lcm := 1
	for n := 2; n <= 20; n++ {
		lcm = Lcm(lcm, n)
	}
	return strconv.Itoa(lcm)
}
