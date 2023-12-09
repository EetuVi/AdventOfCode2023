from Util.file_reader import get_lines


def main():
    file = open("input.txt")
    lines = get_lines(file, True)
    task1(lines)
    task2(lines)


def task1(lines):
    id = 1
    possible_games_array = []
    for line in lines:
        game = line.split(":")[1]
        turns = game.split(";")
        is_valid = validate_game(turns)
        if is_valid:
            possible_games_array.append(id)
        id += 1
    print("Taks 1 answer:", sum(possible_games_array))

def validate_game(turns):
    for turn in turns:
        rolls = turn.split(",")
        for color in rolls:
            single_color = color.strip().split(" ")
            amount = int(single_color[0])
            color = single_color[1]
            if amount > 12 and color == "red":
                return False
            elif amount > 13 and color == "green":
                return False
            elif amount > 14 and color == "blue":
                return False
    return True


def task2(lines):
    power_array = []
    for line in lines:
        game = line.split(":")[1]
        turns = game.split(";")
        minimum_power = calculate_minimum_power(turns)
        power_array.append(minimum_power)
    print("Taks 2 answer:", sum(power_array))


def calculate_minimum_power(turns):
    minimum_red = -1
    minimum_blue = -1
    minimum_green = -1

    for turn in turns:
        rolls = turn.split(",")
        for color in rolls:
            single_color = color.strip().split(" ")
            amount = int(single_color[0])
            color = single_color[1]
            if color == "red":
                if minimum_red == -1 or minimum_red < amount:
                    minimum_red = amount
            elif color == "green":
                if minimum_green == -1 or minimum_green < amount:
                    minimum_green = amount
            elif color == "blue":
                if minimum_blue == -1 or minimum_blue < amount:
                    minimum_blue = amount
    return minimum_red * minimum_blue * minimum_green


if __name__ == '__main__':
    main()