from Util.file_reader import get_lines

def main():
    file = open("input.txt")
    lines = get_lines(file, True)
    task1(lines)
    task2(lines)


def task1(lines):
    value_arr = []
    number = ''
    for line in lines:
        value = ''
        last_number = ''
        for x in line:
            if x.isdigit():
                last_number = x
                if value == '':
                    value += x
        value += last_number
        value_arr.append(int(value))
    print(sum(value_arr))


def task2(lines):
    numbers_dictionary = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    value_arr = []
    number = ''
    for line in lines:
        number_positions = {}
        for key in numbers_dictionary:
            number_positions.update(find_all(line, key, numbers_dictionary[key]))

        value = ''
        last_number = ''
        for x in range(0, len(line)):
            if line[x].isdigit():
                number_positions[x] = line[x]
        sorted_number_positions = dict(sorted(number_positions.items()))
        value_arr.append(int(list(sorted_number_positions.values())[0] + list(sorted_number_positions.values())[-1]))
    # Answer to second task
    print(sum(value_arr))


def find_all(line, number_as_string, number):
    start = 0
    numbers = {}
    while True:
        start = line.find(number_as_string, start)
        if start == -1: return numbers
        numbers[start] = number
        start += len(number_as_string) # use start += 1 to find overlapping matches






if __name__ == '__main__':
    main()