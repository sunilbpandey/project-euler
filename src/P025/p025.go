package problem025

import (
	"math"
	"strconv"
)

func Solve() string {
	phi := (1 + math.Sqrt(float64(5))) / 2
	n := (999*math.Log(10) + math.Log(5)/2) / math.Log(phi)
	return strconv.Itoa(int(math.Ceil(n)))
}
