package problem019

import "strconv"

func getWeekday(day, month, year int) int {
	if month < 3 {
		month += 12
		year--
	}

	century := year / 100
	year %= 100

	dayOfWeek := (day + 13*(month+1)/5 + year + year/4 + century/4 - 2*century) % 7
	if dayOfWeek < 0 {
		return dayOfWeek + 7
	}
	return dayOfWeek
}

func Solve() string {
	sundays := 0
	for year := 1901; year <= 2000; year++ {
		for month := 1; month <= 12; month++ {
			if getWeekday(1, month, year) == 0 {
				sundays++
			}
		}
	}
	return strconv.Itoa(sundays)
}
