import re

puzzle_input = "input.txt"

with open(puzzle_input, "r") as f:
    data = f.readlines()

## Part 1
total_sum = []
pattern = "[1-9]"
for line in data:
    all_digits = re.findall(pattern, line)
   
    first = all_digits[0]
    last = all_digits[-1]
    total_sum.append(int(first+last))

print(sum(total_sum))
