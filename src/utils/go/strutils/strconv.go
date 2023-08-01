package strutils

import (
	"strconv"

	"github.com/sunilbpandey/project-euler/src/utils/go/errorutils"
)

func Atoi(s string) int {
	n, err := strconv.Atoi(s)
	errorutils.Check(err)
	return n
}
