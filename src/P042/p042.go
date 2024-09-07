package problem042

import (
	"embed"
	"strconv"
	"strings"

	"github.com/sunilbpandey/project-euler/src/utils/go/errorutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/math/intutils"
)

//go:embed p042_words.txt
var content embed.FS

func getWordScore(word string) int {
	score := 0
	for _, c := range word {
		score += int(c) - 'A' + 1
	}
	return score
}

func isPerfectSquare(n int) bool {
	sqrt := intutils.Sqrt(n)
	return sqrt*sqrt == n
}

func Solve() string {
	content, err := content.ReadFile("p042_words.txt")
	errorutils.Check(err)

	count := 0
	words := strings.Split(string(content), ",")
	for _, word := range words {
		word = strings.Trim(word, "\"")
		score := getWordScore(word)
		if isPerfectSquare(8*score + 1) {
			count++
		}
	}
	return strconv.Itoa(count)
}
