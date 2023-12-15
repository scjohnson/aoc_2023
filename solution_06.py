import aocd


def calc_score(time, distance):
    num = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            num += 1
    return num


if __name__ == "__main__":
    input = aocd.get_data(day=6, year=2023)
    # input = "Time:      7  15   30\nDistance:  9  40  200"

    times, distances = [i.split(":")[1].strip() for i in input.split("\n")]

    score = 1
    for time, distance in zip(
        [int(t) for t in times.split()], [int(d) for d in distances.split()]
    ):
        score *= calc_score(time, distance)
    print(score)

    time = int(str.replace(times, " ", ""))
    distance = int(str.replace(distances, " ", ""))
    print(calc_score(time, distance))
