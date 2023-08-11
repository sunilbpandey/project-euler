package sliceutils

func CombinationsWithReplacement[T comparable](list []T, length int) [][]T {
	combinations := make([][]T, 0)
	if length == 1 {
		for _, elem := range list {
			combinations = append(combinations, []T{elem})
		}
		return combinations
	}

	for i, elem := range list {
		for _, combo := range CombinationsWithReplacement(list[i:], length-1) {
			combinations = append(combinations, append([]T{elem}, combo...))
		}
	}
	return combinations
}

func Equal[T comparable](a, b []T) bool {
	if len(a) != len(b) {
		return false
	}

	for i, value := range a {
		if value != b[i] {
			return false
		}
	}
	return true
}
