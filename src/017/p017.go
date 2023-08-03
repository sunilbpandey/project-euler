package problem017

import "strconv"

var numberNames = map[int]string{
	1:  "one",
	2:  "two",
	3:  "three",
	4:  "four",
	5:  "five",
	6:  "six",
	7:  "seven",
	8:  "eight",
	9:  "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
}

func getNumberName(number int) string {
	name, found := numberNames[number]
	if found {
		return name
	}

	if number < 100 {
		units := number % 10
		name := numberNames[number-units]
		if units > 0 {
			name += numberNames[units]
		}
		return name
	}

	if number < 1000 {
		tens := number % 100
		name := numberNames[number/100] + "hundred"
		if tens > 0 {
			name += "and" + getNumberName(tens)
		}
		return name
	}
	return "onethousand"
}

func Solve() string {
	letterCount := 0
	for n := 1; n <= 1000; n++ {
		name := getNumberName(n)
		letterCount += len(name)
	}
	return strconv.Itoa(letterCount)
}
