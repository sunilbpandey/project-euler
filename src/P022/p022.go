package problem022

import (
	"embed"
	"sort"
	"strconv"
	"strings"

	"github.com/sunilbpandey/project-euler/src/utils/go/errorutils"
)

//go:embed p022_names.txt
var content embed.FS

func getNameValue(name string) int {
	value := 0
	for _, c := range name {
		value += int(c) - 'A' + 1
	}
	return value
}

func Solve() string {
	content, err := content.ReadFile("p022_names.txt")
	errorutils.Check(err)

	score := 0
	names := strings.Split(string(content), ",")
	sort.Strings(names)
	for i, name := range names {
		name = strings.Trim(name, "\"")
		score += getNameValue(name) * (i + 1)
	}
	return strconv.Itoa(score)
}
