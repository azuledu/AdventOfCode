def main1():
    # input_file = open("test_input.txt", "r")
    input_file = open("input.txt", "r")

    total_points = 0
    while True:
        line = input_file.readline()
        if not line:
            print("Sum: ", total_points)
            break
        else:
            winning_numbers = list(map(int, line.split(":")[1].split("|")[0].split()))
            my_numbers = list(map(int, line.split(":")[1].split("|")[1].split()))
            my_winning_numbers = list(
                filter(lambda number: number in winning_numbers, my_numbers)
            )

            points = 0
            if len(my_winning_numbers) == 1:
                points = 1
            if len(my_winning_numbers) > 1:
                points = 2 ** (len(my_winning_numbers) - 1)

            total_points += points
            print(points)

            # total_points += 2 ** (len(my_winning_numbers) - 1) if len(my_winning_numbers) > 0 else 0

    input_file.close()

    # total_points += 2 ** (len(my_winning_numbers) - 1) if len(my_winning_numbers) > 0 else 0


def main2():
    input_file = open("test_input.txt", "r")
    # input_file = open("input.txt", "r")

    num_of_initial_scratchcards = len(input_file.readlines())
    scratchcards = [1] * num_of_initial_scratchcards

    total_points = 0
    while True:
        line = input_file.readline()
        if not line:
            print("Scratchcards: ", total_points)
            break
        else:
            print(line)

    input_file.close()


if __name__ == "__main__":
    # main1()
    main2()
