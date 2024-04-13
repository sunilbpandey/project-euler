package problem059

import (
	"embed"
	"strconv"
	"strings"

	"github.com/sunilbpandey/project-euler/src/utils/go/errorutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/strutils"
)

//go:embed p059_cipher.txt
var file embed.FS

var disallowedChars = map[int]bool{
	'@':  true,
	'`':  true,
	'\\': true,
}

func decrypt(cipherText, key []int) []int {
	plainText := make([]int, len(cipherText))
	for i, c := range cipherText {
		k := int('a') + key[i%3]
		plainText[i] = c ^ k
		if plainText[i] < int(' ') || plainText[i] > int('z') || disallowedChars[plainText[i]] {
			return nil
		}
	}
	return plainText
}

func Solve() string {
	content, err := file.ReadFile("p059_cipher.txt")
	errorutils.Check(err)

	letters := strings.Split(string(content), ",")
	cipherText := make([]int, len(letters))
	for i, letter := range letters {
		cipherText[i] = strutils.Atoi(letter)
	}

	var plainText []int
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			for k := 0; k < 26; k++ {
				plainText = decrypt(cipherText, []int{i, j, k})
				if plainText != nil {
					sum := 0
					for _, c := range plainText {
						sum += c
					}
					return strconv.Itoa(sum)
				}
			}
		}
	}
	return ""
}
