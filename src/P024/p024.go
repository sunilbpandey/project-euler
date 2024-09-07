package problem024

import (
	"strconv"
	"strings"

	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

func Solve() string {
	answer := make([]string, 0)

	digits := make([]string, 10)
	for i := 0; i < 10; i++ {
		digits[i] = strconv.Itoa(i)
	}

	permutations := 999999
	for len(digits) > 0 {
		factorial := intutils.Factorial(len(digits) - 1)

		index := permutations / factorial
		answer = append(answer, digits[index])
		digits = append(digits[:index], digits[index+1:]...)

		permutations %= factorial
	}
	return strings.Join(answer, "")
}
