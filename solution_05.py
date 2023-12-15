import bisect

import aocd

if __name__ == "__main__":
    input = aocd.get_data(day=5, year=2023)
    # input ="seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4\n"

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

            def add_map(m):
                if 0 not in m:
                    m[0] = [0,0]
                m[max(m.keys()) + m[max(m.keys())][1]] = [
                    max(m.keys()) + m[max(m.keys())][1],
                    0,
                ]
                return m
            maps.append(add_map(new_map))
            reverse_maps.insert(0, add_map(new_reverse_map))

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

    def value_in_ranges(value):
        for i, j in zip(mins, maxs):
            if i <= value <= j:
                return True
        return False

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
        if value_in_ranges(lookup):
            print("part 2: ", check)
            break
        check += 1
