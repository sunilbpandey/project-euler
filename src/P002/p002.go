package problem002

import "strconv"

func Solve() string {
	prev, curr := 1, 1
	for curr < 4000000 {
		prev, curr = curr, prev+curr
	}

	if curr%2 == 0 {
		curr = prev
	} else if prev%2 == 0 {
		curr += prev
	}
	return strconv.Itoa((curr - 1) / 2)
}
