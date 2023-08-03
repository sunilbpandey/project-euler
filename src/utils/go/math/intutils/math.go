package intutils

import "math"

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

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func Pow(x int, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func Sqrt(n int) int {
	return int(math.Sqrt(float64(n)))
}
