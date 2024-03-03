import re


def get_line_numbers(line: str) -> list[str]:
    return re.findall(r'\d+', line)


def get_part_numbers(line: str) -> list[str]:
    part_numbers = []
    numbers = get_line_numbers(line)
    for number in numbers:
        number_index = line.find(number)
        if number_index != -1 and number_index > 0 and line[number_index - 1] != '.':
            part_numbers.append(number)
        elif number_index != -1 and number_index < len(line) and line[number_index + len(number)] != '.':
            part_numbers.append(number)

    return part_numbers


def is_adjacent_to_a_symbol_from_the_same_line(line: str, number: str) -> bool:
    extended_line = '.' + line.strip() + '.'
    number_index = extended_line.find(number)
    if number_index == -1:
        return False  # number not found in line
    elif extended_line[number_index - 1] != '.' or extended_line[number_index + len(number)] != '.':
        return True  # number adjacent to a symbol
    else:
        return False  # number not adjacent to a symbol

    # number_index = line.find(number)
    # if number_index != -1 and number_index > 0 and line[number_index - 1] != '.':
    #     return True
    # elif number_index != -1 and number_index < len(line) and line[number_index + len(number)] != '.':
    #     return True
    # return False


def is_adjacent_to_a_symbol_from_other_line(line: str, other_line: str, number: str) -> bool:
    extended_other_line = '.' + other_line.strip() + '.'
    number_index = line.find(number)
    if number_index == -1:
        return False  # number not found in line
    else:
        symbol = re.search(r'[^.0-9]', extended_other_line[number_index:(number_index + len(number) + 2)])
        return False if (symbol is None) else True


def main():
    # input_file = open("test_input.txt", "r")
    # input_file = open("test_input_reddit.txt", "r")
    input_file = open("input.txt", "r")

    part_numbers = [0]
    line = input_file.readline().strip()
    next_line = input_file.readline().strip()

    # Process first two lines
    numbers = get_line_numbers(line)
    for number in numbers:
        if (is_adjacent_to_a_symbol_from_the_same_line(line, number)
                or is_adjacent_to_a_symbol_from_other_line(line, next_line, number)):
            part_numbers.append(int(number))
        line = line.replace(number, '.' * len(number), 1)  # To avoid problems detecting 'numbers inside numbers' (i.e. 12 and 1)

    while True:
        previous_line = line
        line = next_line
        next_line = input_file.readline().strip()

        if not next_line:
            # Process last two lines
            numbers = get_line_numbers(line)
            for number in numbers:
                if (is_adjacent_to_a_symbol_from_the_same_line(line, number)
                        or is_adjacent_to_a_symbol_from_other_line(line, previous_line, number)):
                    part_numbers.append(int(number))
                line = line.replace(number, '.' * len(number), 1)
            print(part_numbers)
            print('sum: ', sum(part_numbers))
            break
        else:
            numbers = get_line_numbers(line)
            for number in numbers:
                if (is_adjacent_to_a_symbol_from_the_same_line(line, number)
                        or is_adjacent_to_a_symbol_from_other_line(line, previous_line, number)
                        or is_adjacent_to_a_symbol_from_other_line(line, next_line, number)):
                    part_numbers.append(int(number))
                line = line.replace(number, '.' * len(number), 1)

    input_file.close()


def adjacent_to_an_asterisk_from_the_same_line(line: str, number: str) -> int | None:
    extended_line = '.' + line.strip() + '.'
    number_index = extended_line.find(number)
    if number_index == -1:
        return None  # number not found in line
    elif extended_line[number_index - 1] == '*':
        asterisk_index = number_index - 1
    elif extended_line[number_index + len(number)] == '*':
        asterisk_index = number_index + len(number)
    else:
        return None  # number not adjacent to an asterisk

    return asterisk_index


def adjacent_to_an_asterisk_from_other_line(line: str, other_line: str, number: str) -> int | None:
    extended_other_line = '.' + other_line.strip() + '.'
    number_index = line.find(number)
    if number_index == -1:
        return None  # number not found in line
    else:
        asterisk = re.search(r'\*', extended_other_line[number_index:(number_index + len(number) + 2)])
        return None if (asterisk is None) else number_index + asterisk.span()[0]


def main2():
    # input_file = open("test_input.txt", "r")
    # input_file = open("test_input_reddit.txt", "r")  # Part 1: 925 - Part 2: 6756
    input_file = open("input.txt", "r")

    gears: dict[str, list] = {}
    line_number = 1
    line = input_file.readline().strip()
    next_line = input_file.readline().strip()

    # Process first two lines
    numbers = get_line_numbers(line)
    for number in numbers:
        asterisk_index = adjacent_to_an_asterisk_from_the_same_line(line, number)
        if asterisk_index is not None:
            gears = add_gear(asterisk_index, gears, line_number, number)

        asterisk_index = adjacent_to_an_asterisk_from_other_line(line, next_line, number)
        if asterisk_index is not None:
            gears = add_gear(asterisk_index, gears, line_number + 1, number)

        line = line.replace(number, '.' * len(number), 1)  # To avoid problems detecting 'numbers inside numbers' (i.e. 12 and 1)

    while True:
        previous_line = line
        line = next_line
        next_line = input_file.readline().strip()
        line_number += 1

        if not next_line:
            # Process last two lines
            numbers = get_line_numbers(line)
            for number in numbers:
                asterisk_index = adjacent_to_an_asterisk_from_the_same_line(line, number)
                if asterisk_index is not None:
                    gears = add_gear(asterisk_index, gears, line_number, number)

                asterisk_index = adjacent_to_an_asterisk_from_other_line(line, previous_line, number)
                if asterisk_index is not None:
                    gears = add_gear(asterisk_index, gears, line_number - 1, number)

            print(gears)
            gear_ratios = [0]
            for key, value in gears.items():
                if len(value) == 2:
                    gear_ratios += [value[0] * value[1]]
            print('sum: ', sum(gear_ratios))
            break
        else:
            numbers = get_line_numbers(line)
            for number in numbers:
                asterisk_index = adjacent_to_an_asterisk_from_the_same_line(line, number)
                if asterisk_index is not None:
                    gears = add_gear(asterisk_index, gears, line_number, number)

                asterisk_index = adjacent_to_an_asterisk_from_other_line(line, previous_line, number)
                if asterisk_index is not None:
                    gears = add_gear(asterisk_index, gears, line_number - 1, number)

                asterisk_index = adjacent_to_an_asterisk_from_other_line(line, next_line, number)
                if asterisk_index is not None:
                    gears = add_gear(asterisk_index, gears, line_number + 1, number)

                line = line.replace(number, '.' * len(number), 1)

    input_file.close()


def add_gear(asterisk_index, gears, line_number, number):
    key = 'l' + str(line_number) + 'i' + str(asterisk_index)
    gears[key] = (gears[key] + [int(number)]) if key in gears.keys() else [int(number)]
    # if key in gears.keys():
    #     gears[key] = gears[key] + [int(number)]
    # else:
    #     gears[key] = [int(number)]
    return gears


if __name__ == '__main__':
    # main()
    main2()
