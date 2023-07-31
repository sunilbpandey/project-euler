package projecteuler_test

import (
	"encoding/json"
	"fmt"
	"os"
	"testing"

	"github.com/sunilbpandey/project-euler/src/utils/go"
)

type Record struct {
	Problem int    `json:"problem"`
	Answer  string `json:"answer"`
}

func ReadAnswers() map[int]string {
	file, err := os.Open("../answers.json")
	errorutils.Check(err)
	defer file.Close()

	var records []Record
	err = json.NewDecoder(file).Decode(&records)
	errorutils.Check(err)

	var answers = make(map[int]string)
	for _, record := range records {
		answers[record.Problem] = record.Answer
	}
	return answers
}

func TestProblems(t *testing.T) {
	answers := ReadAnswers()
	for number, problem := range problemFuncs {
		t.Run(fmt.Sprintf("Problem %03v", number), func(t *testing.T) {
			if result := problem(); result != answers[number] {
				t.Errorf("expected: %s, got: %s", answers[number], result)
			}
		})
	}
}
