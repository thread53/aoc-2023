RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

puzzle_input = "input.txt"

with open(puzzle_input, "r") as f:
    data = f.readlines()

## Part 1
ids_sum = 0

for line in data:
    game_data = line.split(":")
    game_id = int(game_data[0].split()[1])
    is_valid = True
    for game_set in game_data[1].split(";"):
        for cubes_set in game_set.split(","):
            points = int(cubes_set.split()[0])
            cube_color = cubes_set.split()[1]
            if cube_color == "red" and points > RED_LIMIT:
                is_valid = False
            if cube_color == "green" and points > GREEN_LIMIT:
                is_valid = False
            if cube_color == "blue" and points > BLUE_LIMIT:
                is_valid = False

    if is_valid:    
        ids_sum += game_id

print(ids_sum)


## Part 2
power_sum = 0

for line in data:
    game_data = line.split(":")
    red_min = -999999
    green_min = -999999
    blue_min = -999999
    for game_set in game_data[1].split(";"):
        for cubes_set in game_set.split(","):
            points = int(cubes_set.split()[0])
            cube_color = cubes_set.split()[1]
            if cube_color == "red" and points > red_min:
                red_min = points
            if cube_color == "green" and points > green_min:
                green_min = points
            if cube_color == "blue" and points > blue_min:
                blue_min = points

    power_sum += red_min * green_min * blue_min

print(power_sum)