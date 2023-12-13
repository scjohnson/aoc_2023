import aocd


def below_max(cube):
    num, type = cube.split(" ")
    num = int(num)
    if type == "red" and num > 12:
        return False
    if type == "green" and num > 13:
        return False
    if type == "blue" and num > 14:
        return False
    return True


def min_score(games):
    mins = {"red": 0, "green": 0, "blue": 0}

    def insert_min(game):
        cubes = game.split(", ")
        for cube in cubes:
            num, type = cube.split(" ")
            num = int(num)
            mins[type] = max(num, mins[type])

    for game in games.split("; "):
        insert_min(game)
        values = list(mins.values())
    return values[0] * values[1] * values[2]


if __name__ == "__main__":
    input = aocd.get_data(day=2, year=2023)
    score = 0
    score2 = 0
    for line in input.split("\n"):
        first, second = line.split(": ")
        id = int(first.split(" ")[1])
        test = []
        for game in second.split("; "):
            test.extend([below_max(cubes) for cubes in game.split(", ")])
        score2 += min_score(second)
        if all(test):
            score += id
    print(score, score2)
