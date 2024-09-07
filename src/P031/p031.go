package problem031

import "strconv"

func Solve() string {
	coins := []int{1, 2, 5, 10, 20, 50, 100, 200}

	amount := 200
	ways := make([]int, amount+1)
	ways[0] = 1
	for _, coin := range coins {
		for target := coin; target <= amount; target++ {
			ways[target] += ways[target-coin]
		}
	}
	return strconv.Itoa(ways[amount])
}
