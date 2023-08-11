package strutils

import (
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
