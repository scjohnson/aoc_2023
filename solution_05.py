import bisect

import aocd


def parse_input(input):
    seeds = []
    maps = []
    reverse_maps = []
    lines = input.split("\n")
    for index, line in enumerate(lines):
        if "seeds:" in line:
            seeds = line.split(": ")[1]
            seeds = [int(s) for s in seeds.split()]
        if "map" in line:
            n = index + 1
            new_map = {}
            new_reverse_map = {}
            while n < len(lines) and lines[n].strip() != "":
                f, s, t = lines[n].split()
                new_map[int(s)] = [int(f), int(t)]
                new_reverse_map[int(f)] = [int(s), int(t)]
                n += 1
            maps.append(add_map(new_map))
            reverse_maps.insert(0, add_map(new_reverse_map))
    return seeds, maps, reverse_maps


def add_map(m):
    if 0 not in m:
        m[0] = [0, 0]
    m[max(m.keys()) + m[max(m.keys())][1]] = [
        max(m.keys()) + m[max(m.keys())][1],
        0,
    ]
    return m


def value_in_ranges(value, mins, maxs):
    for i, j in zip(mins, maxs):
        if i <= value <= j:
            return True
    return False


def main():
    input = aocd.get_data(day=5, year=2023)
    seeds, maps, reverse_maps = parse_input(input)

    next_lookups = seeds.copy()
    for m in maps:
        lookups = next_lookups.copy()
        next_lookups = []
        for lookup in lookups:
            if lookup in m:
                value = lookup
            else:
                sorted_map = sorted(m)
                i = bisect.bisect_left(sorted_map, lookup)
                value = sorted_map[i - 1]
            next_lookups.append(lookup - value + m[value][0])
    print("part 1: ", min(next_lookups))

    mins = []
    maxs = []
    for ran in range(len(seeds) // 2):
        mins.append(seeds[2 * ran])
        maxs.append(seeds[2 * ran] + seeds[2 * ran + 1])

    # I AM BRUUUTE
    check = 0
    while True:
        lookup = check
        for m in reverse_maps:
            if lookup in m:
                value = lookup
            else:
                sorted_map = sorted(m)
                i = bisect.bisect_left(sorted_map, lookup)
                value = sorted_map[i - 1]
            lookup = lookup - value + m[value][0]
        if value_in_ranges(lookup, mins, maxs):
            print("part 2: ", check)
            break
        check += 1


if __name__ == "__main__":
    main()
