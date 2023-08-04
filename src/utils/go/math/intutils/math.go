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

func SumOfDivisors(n int) int {
	sum := 0
	for d := 1; d < Sqrt(n)+1; d++ {
		if n%d == 0 {
			sum += d
			if n/d != d {
				sum += n / d
			}
		}
	}
	return sum
}

func SumOfProperDivisors(n int) int {
	return SumOfDivisors(n) - n
}
