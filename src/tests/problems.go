package projecteuler_test

import (
	problem001 "github.com/sunilbpandey/project-euler/src/001"
	problem002 "github.com/sunilbpandey/project-euler/src/002"
	problem003 "github.com/sunilbpandey/project-euler/src/003"
	problem004 "github.com/sunilbpandey/project-euler/src/004"
	problem005 "github.com/sunilbpandey/project-euler/src/005"
	problem006 "github.com/sunilbpandey/project-euler/src/006"
	problem007 "github.com/sunilbpandey/project-euler/src/007"
	problem008 "github.com/sunilbpandey/project-euler/src/008"
	problem009 "github.com/sunilbpandey/project-euler/src/009"
	problem010 "github.com/sunilbpandey/project-euler/src/010"
	problem011 "github.com/sunilbpandey/project-euler/src/011"
	problem012 "github.com/sunilbpandey/project-euler/src/012"
	problem013 "github.com/sunilbpandey/project-euler/src/013"
	problem014 "github.com/sunilbpandey/project-euler/src/014"
	problem015 "github.com/sunilbpandey/project-euler/src/015"
	problem016 "github.com/sunilbpandey/project-euler/src/016"
	problem017 "github.com/sunilbpandey/project-euler/src/017"
	problem018 "github.com/sunilbpandey/project-euler/src/018"
	problem019 "github.com/sunilbpandey/project-euler/src/019"
	problem020 "github.com/sunilbpandey/project-euler/src/020"
	problem021 "github.com/sunilbpandey/project-euler/src/021"
	problem022 "github.com/sunilbpandey/project-euler/src/022"
	problem023 "github.com/sunilbpandey/project-euler/src/023"
	problem024 "github.com/sunilbpandey/project-euler/src/024"
	problem025 "github.com/sunilbpandey/project-euler/src/025"
	problem026 "github.com/sunilbpandey/project-euler/src/026"
	problem027 "github.com/sunilbpandey/project-euler/src/027"
	problem028 "github.com/sunilbpandey/project-euler/src/028"
	problem029 "github.com/sunilbpandey/project-euler/src/029"
	problem030 "github.com/sunilbpandey/project-euler/src/030"
	problem031 "github.com/sunilbpandey/project-euler/src/031"
)

type ProblemFunc func() string

var problemFuncs = map[int]ProblemFunc{
	1:  problem001.Solve,
	2:  problem002.Solve,
	3:  problem003.Solve,
	4:  problem004.Solve,
	5:  problem005.Solve,
	6:  problem006.Solve,
	7:  problem007.Solve,
	8:  problem008.Solve,
	9:  problem009.Solve,
	10: problem010.Solve,
	11: problem011.Solve,
	12: problem012.Solve,
	13: problem013.Solve,
	14: problem014.Solve,
	15: problem015.Solve,
	16: problem016.Solve,
	17: problem017.Solve,
	18: problem018.Solve,
	19: problem019.Solve,
	20: problem020.Solve,
	21: problem021.Solve,
	22: problem022.Solve,
	23: problem023.Solve,
	24: problem024.Solve,
	25: problem025.Solve,
	26: problem026.Solve,
	27: problem027.Solve,
	28: problem028.Solve,
	29: problem029.Solve,
	30: problem030.Solve,
	31: problem031.Solve,
}
