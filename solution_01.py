import aocd

NUMS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}


def isdigit(line):
    for k, v in NUMS.items():
        if line.startswith(k):
            return v, line[len(k) :]
    return False, line[1:]


if __name__ == "__main__":
    input = aocd.get_data(day=1, year=2023)

    tot = 0
    for line in input.split("\n"):
        nums = [int(l) for l in line if l.isdigit()]
        tot += nums[0] * 10 + nums[-1]
    print(tot)

    tot = 0
    for line in input.split("\n"):
        nums = []
        while len(line) > 0:
            digit, line = isdigit(line)
            if digit:
                nums.append(digit)
        tot += nums[0] * 10 + nums[-1]
    print(tot)
