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
	"github.com/sunilbpandey/project-euler/src/012"
	"github.com/sunilbpandey/project-euler/src/013"
	"github.com/sunilbpandey/project-euler/src/014"
	"github.com/sunilbpandey/project-euler/src/015"
	"github.com/sunilbpandey/project-euler/src/016"
	"github.com/sunilbpandey/project-euler/src/017"
	"github.com/sunilbpandey/project-euler/src/018"
	"github.com/sunilbpandey/project-euler/src/019"
	"github.com/sunilbpandey/project-euler/src/020"
	"github.com/sunilbpandey/project-euler/src/021"
	"github.com/sunilbpandey/project-euler/src/022"
	"github.com/sunilbpandey/project-euler/src/023"
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
}
