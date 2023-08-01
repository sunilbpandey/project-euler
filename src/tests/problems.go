package projecteuler_test

import (
	"github.com/sunilbpandey/project-euler/src/001"
	"github.com/sunilbpandey/project-euler/src/002"
	"github.com/sunilbpandey/project-euler/src/003"
	"github.com/sunilbpandey/project-euler/src/004"
	"github.com/sunilbpandey/project-euler/src/005"
	"github.com/sunilbpandey/project-euler/src/006"
	"github.com/sunilbpandey/project-euler/src/007"
	"github.com/sunilbpandey/project-euler/src/008"
	"github.com/sunilbpandey/project-euler/src/009"
	"github.com/sunilbpandey/project-euler/src/010"
	"github.com/sunilbpandey/project-euler/src/011"
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
}
