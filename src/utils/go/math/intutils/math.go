package intutils

import (
	"math"
	"strconv"
)

func Digits(n interface{}) []int {
	var str string
	switch n.(type) {
	case int:
		str = strconv.Itoa(n.(int))
	case string:
		str = n.(string)
	default:
		panic("Unsupported type")
	}

	digits := make([]int, len(str))
	for i, digit := range str {
		digits[i] = int(digit - '0')
	}
	return digits
}

func Factorial(n int) int {
	factorial := 1
	for m := 2; m <= n; m++ {
		factorial *= m
	}
	return factorial
}

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
