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
