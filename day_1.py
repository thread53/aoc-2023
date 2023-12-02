import re

puzzle_input = "input.txt"

with open(puzzle_input, "r") as f:
    data = f.readlines()

## Part 1
total_sum = 0
pattern = "[1-9]"
for line in data:
    all_digits = re.findall(pattern, line)
    first = all_digits[0]
    last = all_digits[-1]
    total_sum += (int(first+last))

print(total_sum)


## Part 2
mapper = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
}

total_sum = 0
pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"

for line in data:
    all_digits = re.findall(pattern, line)
    first = all_digits[0]
    last = all_digits[-1]
    
    if first in mapper.keys():
        first = mapper[first]

    if last in mapper.keys():
        last = mapper[last]

    total_sum += (int(first+last))

print(total_sum)