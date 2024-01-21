import re


def calibrate(line: str):
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    line_numbers_to_digits_forward = ''

    # First digit
    for char in line:
        line_numbers_to_digits_forward += char
        for key in numbers.keys():
            line_numbers_to_digits_forward = line_numbers_to_digits_forward.replace(key, numbers[key])
    line_digits_forward = re.sub("[^1-9]", "", line_numbers_to_digits_forward)
    first_digit = line_digits_forward[0]

    # Last digit
    line_numbers_to_digits_backward = ''
    for char in line[::-1]:
        line_numbers_to_digits_backward = char + line_numbers_to_digits_backward
        for key in numbers.keys():
            line_numbers_to_digits_backward = line_numbers_to_digits_backward.replace(key, numbers[key])
    line_digits_backward = re.sub("[^1-9]", "", line_numbers_to_digits_backward)
    last_digit = line_digits_backward[-1]

    return int(first_digit + last_digit)


if __name__ == '__main__':
    input_file = open("input.txt", "r")

    sum = 0
    while True:
        line = input_file.readline()
        if not line:
            print("Sum: ", sum)
            break
        else:
            sum += calibrate(line)

    input_file.close()
