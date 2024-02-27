import random


GO = 0
JAIL = 10
G2J = 30

C1 = 11
E3 = 24
H2 = 39
R1 = 5

CH = [7, 22, 36]
CC = [2, 17, 33]
R = [5, 15, 25, 35]
U = [12, 28]

CH_CARDS = [GO, JAIL, C1, E3, H2, R1]
CC_CARDS = [GO, JAIL]


# pylint: disable=too-many-branches
def solve() -> int:
    visits = [0] * 40
    position = 0

    ch_cards = list(range(16))
    random.shuffle(ch_cards)

    cc_cards = list(range(16))
    random.shuffle(cc_cards)

    doubles = 0
    for _ in range(1000000):
        roll1 = random.randint(1, 4)
        roll2 = random.randint(1, 4)
        if roll1 == roll2:
            doubles += 1
            if doubles < 3:
                continue
            position = JAIL
            doubles = 0
        else:
            doubles = 0
            position = (position + roll1 + roll2) % 40

        if position == G2J:
            position = JAIL
        elif position in CH:
            card = cc_cards.pop(0)
            if card < len(CH_CARDS):
                position = CH_CARDS[card]
            elif card in (6, 7):
                if position == CH[0]:
                    position = R[1]
                elif position == CH[1]:
                    position = R[2]
                else:
                    position = R[0]
            elif card == 8:
                position = U[1] if position == CH[1] else U[0]
            elif card == 9:
                position -= 3
                if position < 0:
                    position += 40
            cc_cards.append(card)
        elif position in CC:
            card = cc_cards.pop(0)
            if card < len(CC_CARDS):
                position = CC_CARDS[card]
            cc_cards.append(card)

        visits[position] += 1
    indices = sorted(list(range(40)), key=lambda i: visits[i], reverse=True)
    return int("".join(f"{i:02}" for i in indices[:3]))
