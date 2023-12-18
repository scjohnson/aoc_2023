import functools
from collections import Counter
from itertools import product

import aocd
import numpy as np


def second_compare(h1, h2):
    for i, j in zip(h1, h2):
        if i > j:
            return 1
        elif i < j:
            return -1
    return 0


def compare(hand1, hand2):
    if len(hand1.split(" ")) < 3:
        h1 = hand1.split(" ")[0]
        h2 = hand2.split(" ")[0]
        tb1 = h1
        tb2 = h2
    else:
        h1 = hand1.split(" ")[2]
        h2 = hand2.split(" ")[2]
        tb1 = hand1.split(" ")[0].replace("C", "1")
        tb2 = hand2.split(" ")[0].replace("C", "1")

    counts1 = Counter(h1)
    counts2 = Counter(h2)
    if len(counts1) > len(counts2):
        return -1
    elif len(counts1) < len(counts2):
        return 1

    c1 = [count for _, count in counts1.items()]
    c2 = [count for _, count in counts2.items()]
    if max(c1) > max(c2):
        return 1
    elif max(c1) < max(c2):
        return -1

    return second_compare(tb1, tb2)


def joker_max_hand(hand):
    h = hand.split(" ")[0]
    hjs = [i for i, c in enumerate(h) if c == "C"]

    potential_hands = []

    for replacements in product("23456789BDEF", repeat=len(hjs)):
        new_hand = h
        for c in replacements:
            new_hand = new_hand.replace("C", c, 1)
        new_hand += " a"
        potential_hands.append(new_hand)
    sorted_list = sorted(potential_hands, key=functools.cmp_to_key(compare))
    return sorted_list[-1]


if __name__ == "__main__":
    input = aocd.get_data(day=7, year=2023)
    # input = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"
    input = input.replace("T", "B")
    input = input.replace("J", "C")
    input = input.replace("Q", "D")
    input = input.replace("K", "E")
    input = input.replace("A", "F")
    sorted_list = sorted(input.split("\n"), key=functools.cmp_to_key(compare))

    scores = [int(i.split(" ")[1]) for i in sorted_list]
    place = list(range(1, len(scores) + 1))
    print("part 1: ", np.sum(np.dot(scores, place)))

    joker_hands = []
    for hand in input.split("\n"):
        joker_hands.append(hand + " " + joker_max_hand(hand))
    sorted_list = sorted(joker_hands, key=functools.cmp_to_key(compare))
    scores = [int(i.split(" ")[1]) for i in sorted_list]

    print("part 2: ", np.sum(np.dot(scores, place)))
