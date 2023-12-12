import re

import aocd

if __name__ == "__main__":
    input = aocd.get_data(day=3, year=2023)
    # input = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."

    lines = input.split("\n")
    lines.append("." * len(lines[0]))
    lines.reverse()
    lines.append("." * len(lines[0]))
    lines.reverse()

    chars = "!@#$&%*()=+-_/"

    def nums_locs(line):
        numbers = re.findall("\d+", line)
        locations = [m.start() for m in re.finditer("\d+", line)]
        return zip(locations, numbers)

    total = 0
    for i in range(1, len(lines) - 1):
        for loc, num in nums_locs(lines[i]):
            s = ""
            for j in range(i - 1, i + 2):
                s += lines[j][max(loc - 1, 0) : min(len(lines[j]), loc + len(num) + 1)]
            if any(char in s for char in chars):
                total += int(num)
    print(total)

    total = 0
    for i, line in enumerate(lines[1:-1], start=1):
        for j, char in enumerate(line):
            if char == "*":
                nums = [
                    int(num)
                    for l in lines[i - 1 : i + 2]
                    for loc, num in nums_locs(l)
                    if -1 <= j - loc < len(num) + 1
                ]
                if len(nums) == 2:
                    total += nums[0] * nums[1]
    print(total)
