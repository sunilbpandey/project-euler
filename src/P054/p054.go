package problem054

import (
	"cmp"
	"embed"
	"slices"
	"strconv"
	"strings"

	"github.com/sunilbpandey/project-euler/src/utils/go/errorutils"
	"github.com/sunilbpandey/project-euler/src/utils/go/sliceutils"
)

//go:embed p054_poker.txt
var content embed.FS

type Rank int

const (
	Unknown Rank = iota
	HighCard
	Pair
	TwoPairs
	ThreeOfAKind
	Straight
	Flush
	FullHouse
	FourOfAKind
	StraightFlush
	RoyalFlush
)

type Card struct {
	Value int
	Suit  string
}

func parseCard(card string) Card {
	value := 0
	switch card[0] {
	case 'T':
		value = 10
	case 'J':
		value = 11
	case 'Q':
		value = 12
	case 'K':
		value = 13
	case 'A':
		value = 14
	default:
		value = int(card[0] - '0')
	}
	return Card{value, string(card[1])}
}

func checkForFlush(hand []Card) (Rank, []int) {
	// To check for Flushes, sort by suit and then by value
	slices.SortStableFunc(hand, func(a, b Card) int {
		if a.Suit == b.Suit {
			return cmp.Compare(b.Value, a.Value)
		}
		return cmp.Compare(a.Suit, b.Suit)
	})

	if hand[0].Suit == hand[4].Suit {
		if hand[0].Value == 10 {
			// Royal Flush
			// all royal flushes are equal, so no tie breaker
			return RoyalFlush, nil
		}

		if hand[0].Value-hand[4].Value == 4 {
			// Straight Flush
			return StraightFlush, []int{hand[0].Value}
		}

		// Flush
		return Flush, sliceutils.Map(hand, func(card Card) int {
			return card.Value
		})
	}
	return Unknown, nil
}

func checkForFourOfAKind(cards []int) (Rank, []int) {
	if cards[0] == cards[3] {
		return FourOfAKind, []int{cards[0], cards[4]}
	}
	if cards[1] == cards[4] {
		return FourOfAKind, []int{cards[4], cards[0]}
	}
	return Unknown, nil
}

func checkForFullHouse(cards []int) (Rank, []int) {
	if cards[0] == cards[2] && cards[3] == cards[4] {
		return FullHouse, []int{cards[0], cards[4]}
	}
	if cards[0] == cards[1] && cards[2] == cards[4] {
		return FullHouse, []int{cards[4], cards[0]}
	}
	return Unknown, nil
}

func checkForStraight(cards []int) (Rank, []int) {
	for i := 0; i < 4; i++ {
		if cards[i] != cards[i+1]+1 {
			return Unknown, nil
		}
	}
	return Straight, []int{cards[0]}
}

func checkForThreeOfAKind(cards []int) (Rank, []int) {
	if cards[0] == cards[2] {
		return ThreeOfAKind, []int{cards[0], cards[3], cards[4]}
	}
	if cards[1] == cards[3] {
		return ThreeOfAKind, []int{cards[1], cards[0], cards[4]}
	}
	if cards[2] == cards[4] {
		return ThreeOfAKind, []int{cards[2], cards[0], cards[1]}
	}
	return Unknown, nil
}

func checkForTwoPairs(cards []int) (Rank, []int) {
	if cards[0] == cards[1] && cards[2] == cards[3] {
		return TwoPairs, []int{cards[0], cards[2], cards[4]}
	}
	if cards[0] == cards[1] && cards[3] == cards[4] {
		return TwoPairs, []int{cards[0], cards[3], cards[2]}
	}
	if cards[1] == cards[2] && cards[3] == cards[4] {
		return TwoPairs, []int{cards[1], cards[3], cards[0]}
	}
	return Unknown, nil
}

func checkForPair(cards []int) (Rank, []int) {
	for i := 0; i < 4; i++ {
		if cards[i] == cards[i+1] {
			tieBreakers := []int{cards[i]}
			for j := 0; j < 5; j++ {
				if j != i && j != i+1 {
					tieBreakers = append(tieBreakers, cards[j])
				}
			}
			return Pair, tieBreakers
		}
	}
	return Unknown, nil
}

func classifyHand(hand []Card) (Rank, []int) {
	// Flush
	if rank, cards := checkForFlush(hand); rank != Unknown {
		return rank, cards
	}

	// To check for the remaining ranks, reverse sort by value
	values := sliceutils.Map(hand, func(card Card) int {
		return card.Value
	})
	slices.Sort(values)
	slices.Reverse(values)

	// Four of a Kind
	if rank, cards := checkForFourOfAKind(values); rank != Unknown {
		return rank, cards
	}

	// Full House
	if rank, cards := checkForFullHouse(values); rank != Unknown {
		return rank, cards
	}

	// Straight
	if rank, cards := checkForStraight(values); rank != Unknown {
		return rank, cards
	}

	// Three of a Kind
	if rank, cards := checkForThreeOfAKind(values); rank != Unknown {
		return rank, cards
	}

	// Two Pairs
	if rank, cards := checkForTwoPairs(values); rank != Unknown {
		return rank, cards
	}

	// Pair
	if rank, cards := checkForPair(values); rank != Unknown {
		return rank, cards
	}

	// High Card
	return HighCard, values
}

func compareHands(player1, player2 []Card) int {
	rank1, cards1 := classifyHand(player1)
	rank2, cards2 := classifyHand(player2)

	// if both players have the same ranked hand, compare the card values
	if rank1 == rank2 {
		for i := 0; i < len(cards1); i++ {
			if c := cmp.Compare(cards1[i], cards2[i]); c != 0 {
				return c
			}
		}
	}
	return cmp.Compare(rank1, rank2)
}

func Solve() string {
	content, err := content.ReadFile("p054_poker.txt")
	errorutils.Check(err)

	p1Wins := 0
	for _, line := range strings.Split(string(content), "\n") {
		cards := strings.Split(line, " ")
		if len(cards) != 10 {
			continue
		}

		player1 := sliceutils.Map(cards[:5], parseCard)
		player2 := sliceutils.Map(cards[5:], parseCard)
		if compareHands(player1, player2) > 0 {
			p1Wins++
		}
	}
	return strconv.Itoa(p1Wins)
}
