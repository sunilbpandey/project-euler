package sliceutils

func CombinationsWithReplacement[T comparable](list []T, length int) chan []T {
	ch := make(chan []T)
	go func() {
		if length == 1 {
			for _, elem := range list {
				ch <- []T{elem}
			}
		} else {
			for i, elem := range list {
				for combo := range CombinationsWithReplacement(list[i:], length-1) {
					ch <- append([]T{elem}, combo...)
				}
			}
		}
		close(ch)
	}()
	return ch
}

func Contains[T comparable](list []T, elem T) bool {
	for _, value := range list {
		if value == elem {
			return true
		}
	}
	return false
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

func Permutations[T comparable](list []T, length int) chan []T {
	ch := make(chan []T)

	go func() {
		if length == 0 {
			ch <- []T{}
		} else {
			for i, elem := range list {
				for perm := range Permutations(append(append([]T{}, list[:i]...), list[i+1:]...), length-1) {
					ch <- append([]T{elem}, perm...)
				}
			}
		}
		close(ch)
	}()
	return ch
}

func Product[T comparable](list []T, length int) chan []T {
	ch := make(chan []T)

	go func() {
		if length == 0 {
			ch <- []T{}
		} else if length == 1 {
			for _, elem := range list {
				ch <- []T{elem}
			}
		} else {
			for _, elem := range list {
				for product := range Product(list, length-1) {
					ch <- append([]T{elem}, product...)
				}
			}
		}
		close(ch)
	}()
	return ch
}

func Map[T1, T2 any](list []T1, f func(T1) T2) []T2 {
	result := make([]T2, len(list))
	for i, elem := range list {
		result[i] = f(elem)
	}
	return result
}
