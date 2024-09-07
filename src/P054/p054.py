import os.path
from enum import Enum
from operator import attrgetter


class Rank(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


class Card:  # pylint: disable=too-few-public-methods
    def __init__(self, card: str) -> None:
        self.value = self.__get_card_value(card[0])
        self.suit = card[1]

    def __get_card_value(self, card: str) -> int:
        face_cards = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        return face_cards[card] if card in face_cards else int(card)


def check_for_flush(cards: list[Card]) -> tuple[Rank | None, list[int]]:
    if cards[0].suit == cards[4].suit:
        if cards[0].value == 10:
            # royal flush
            # all royal flushes are equal, so no tie breakers needed
            return Rank.ROYAL_FLUSH, []

        if cards[0].value - cards[4].value == 4:
            # straight flush
            return Rank.STRAIGHT_FLUSH, [cards[0].value]

        # flush
        return Rank.FLUSH, [card.value for card in cards]
    return None, []


def check_for_four_of_a_kind(cards: list[Card]) -> tuple[Rank | None, list[int]]:
    if cards[0].value == cards[3].value:
        # four of a kind
        return Rank.FOUR_OF_A_KIND, [cards[0].value, cards[4].value]

    if cards[1].value == cards[4].value:
        # four of a kind
        return Rank.FOUR_OF_A_KIND, [cards[4].value, cards[0].value]
    return None, []


def check_for_full_house(cards: list[Card]) -> tuple[Rank | None, list[int]]:
    if cards[0].value == cards[2].value and cards[3].value == cards[4].value:
        # full house
        return Rank.FULL_HOUSE, [cards[0].value, cards[4].value]

    if cards[0].value == cards[1].value and cards[2].value == cards[4].value:
        # full house
        return Rank.FULL_HOUSE, [cards[4].value, cards[0].value]
    return None, []


def check_for_three_of_a_kind(cards: list[Card]) -> tuple[Rank | None, list[int]]:
    if cards[0].value == cards[2].value:
        # three of a kind
        return Rank.THREE_OF_A_KIND, [cards[0].value, cards[3].value, cards[4].value]

    if cards[2].value == cards[4].value:
        # three of a kind
        return Rank.THREE_OF_A_KIND, [cards[2].value, cards[0].value, cards[1].value]

    if cards[1].value == cards[3].value:
        # three of a kind
        return Rank.THREE_OF_A_KIND, [cards[1].value, cards[0].value, cards[4].value]
    return None, []


def check_for_straight(cards: list[Card]) -> tuple[Rank | None, list[int]]:
    if all(cards[i].value == cards[i + 1].value + 1 for i in range(4)):
        # straight
        return Rank.STRAIGHT, [cards[0].value]
    return None, []


def check_for_two_pairs(cards: list[Card]) -> tuple[Rank | None, list[int]]:
    if cards[0].value == cards[1].value and cards[2].value == cards[3].value:
        # two pairs
        return Rank.TWO_PAIRS, [cards[0].value, cards[3].value, cards[4].value]

    if cards[0].value == cards[1].value and cards[3].value == cards[4].value:
        # two pairs
        return Rank.TWO_PAIRS, [cards[0].value, cards[3].value, cards[2].value]

    if cards[1].value == cards[2].value and cards[3].value == cards[4].value:
        # two pairs
        return Rank.TWO_PAIRS, [cards[1].value, cards[3].value, cards[0].value]
    return None, []


def check_for_pair(cards: list[Card]) -> tuple[Rank | None, list[int]]:
    for i in range(4):
        if cards[i].value == cards[i + 1].value:
            # pair
            return Rank.PAIR, [cards[i].value] + [
                cards[j].value for j in range(5) if j != i
            ]
    return None, []


def classify(cards: list[Card]) -> tuple[Rank, list[int]]:
    # Sort the cards by value and suit
    cards = sorted(cards, key=attrgetter("value"), reverse=True)
    cards = sorted(cards, key=attrgetter("suit"))

    (rank, tie_breakers) = check_for_flush(cards)
    if rank is not None:
        return rank, tie_breakers

    # Now sort just by value
    cards = sorted(cards, key=attrgetter("value"), reverse=True)

    checkers = [
        check_for_four_of_a_kind,
        check_for_full_house,
        check_for_three_of_a_kind,
        check_for_straight,
        check_for_two_pairs,
        check_for_pair,
    ]
    for checker in checkers:
        (rank, tie_breakers) = checker(cards)
        if rank is not None:
            return rank, tie_breakers

    # high card
    return Rank.HIGH_CARD, [card.value for card in cards]


def compare_hands(hand1: list[Card], hand2: list[Card]) -> int:
    (rank1, values1) = classify(hand1)
    (rank2, values2) = classify(hand2)

    if rank1.value > rank2.value:
        # player 1 has higher ranked hand
        return -1

    if rank1.value < rank2.value:
        # player 2 has higher ranked hand
        return 1

    # both players have the same ranked hand, so compare the card values
    for value1, value2 in zip(values1, values2):
        if value1 > value2:
            return -1
        if value1 < value2:
            return 1
    return 0


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "p054_poker.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    total = 0
    for line in content.split("\n"):
        cards = line.split(" ")
        if len(cards) != 10:
            continue

        player1 = [Card(card) for card in cards[:5]]
        player2 = [Card(card) for card in cards[5:]]
        if compare_hands(player1, player2) == -1:
            total += 1

    return total
