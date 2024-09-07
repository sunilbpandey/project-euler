package problem053

import "strconv"

func Solve() string {
	count := 0
	row := make([]int, 0)
	for n := 0; n < 101; n++ {
		row = append([]int{1}, row...)
		for i := 1; i < len(row)-1; i++ {
			row[i] += row[i+1]
			if row[i] > 1000000 {
				count += n - 2*i + 1
				break
			}
		}
	}
	return strconv.Itoa(count)
}
