import aocd
import numpy as np

if __name__ == "__main__":
    input = aocd.get_data(day=4, year=2023)
    # input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

    input_length = len(input.split("\n"))
    copies = np.ones(input_length)
    total = 0
    for index, game in enumerate(input.split("\n")):
        hand = game.split(": ")[1]
        winners, hand = hand.split(" | ")
        winners = [int(i) for i in winners.split()]
        hand = [int(i) for i in hand.split()]
        score = 0
        for winner in winners:
            if winner in hand:
                score += 1
        if score > 0:
            total += 2 ** (score - 1)
            copies[index + 1 : min(index + score + 1, input_length)] += copies[index]
    print(total, int(sum(copies[0:input_length])))
