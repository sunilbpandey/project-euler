package problem036

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

func makeBinaryPalindrome(n int, oddLength bool) int {
	result := n
	if oddLength {
		n /= 2
	}

	for n > 0 {
		result = result*2 + n%2
		n /= 2
	}
	return result
}

func makeBinaryPalindromes(limit int, oddLength bool) chan int {
	ch := make(chan int)
	go func() {
		for n := 1; ; n++ {
			palindrome := makeBinaryPalindrome(n, oddLength)
			if palindrome > limit {
				break
			}
			ch <- palindrome
		}
		close(ch)
	}()
	return ch
}

func Solve() string {
	sum := 0
	for _, oddLength := range []bool{true, false} {
		for palindrome := range makeBinaryPalindromes(1000000, oddLength) {
			if strutils.IsPalindrome(strconv.Itoa(palindrome)) {
				sum += palindrome
			}
		}
	}
	return strconv.Itoa(sum)
}
