package projecteuler_test

import (
	"github.com/sunilbpandey/project-euler/src/001"
	"github.com/sunilbpandey/project-euler/src/002"
	"github.com/sunilbpandey/project-euler/src/003"
	"github.com/sunilbpandey/project-euler/src/004"
	"github.com/sunilbpandey/project-euler/src/005"
)

type ProblemFunc func() string

var problemFuncs = map[int]ProblemFunc{
	1: problem001.Solve,
	2: problem002.Solve,
	3: problem003.Solve,
	4: problem004.Solve,
	5: problem005.Solve,
}
