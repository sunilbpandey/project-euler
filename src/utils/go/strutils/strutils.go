package strutils

import (
	"slices"
	"strconv"
	"strings"

	"github.com/sunilbpandey/project-euler/src/utils/go/errorutils"
)

func Atoi(s string) int {
	n, err := strconv.Atoi(s)
	errorutils.Check(err)
	return n
}

func JoinInts(list []int) string {
	strs := make([]string, len(list))
	for i, n := range list {
		strs[i] = strconv.Itoa(n)
	}
	return strings.Join(strs, "")
}

func IsPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func Reverse(s string) string {
	bytes := []byte(s)
	slices.Reverse(bytes)
	return string(bytes)
}
