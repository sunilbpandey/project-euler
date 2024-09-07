package problem009

import "strconv"

func Solve() string {
	product := 0
	for m := 1; m < 22 && product == 0; m++ {
		for n := 1; n < m && product == 0; n++ {
			if m*(m+n) == 500 {
				a := m*m - n*n
				b := 2 * m * n
				c := m*m + n*n
				product = a * b * c
			}
		}
	}
	return strconv.Itoa(product)
}
