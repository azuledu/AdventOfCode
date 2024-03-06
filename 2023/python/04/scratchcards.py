from functools import reduce


def main():
    #input_file = open("test_input.txt", "r")
    input_file = open("input.txt", "r")

    total_points = 0
    while True:
        line = input_file.readline()
        if not line:
            print('Sum: ', total_points)
            break
        else:
            winning_numbers = list(map(int, line.split(':')[1].split('|')[0].split()))
            my_numbers = list(map(int, line.split(':')[1].split('|')[1].split()))
            my_winning_numbers = list(filter(lambda number: number in winning_numbers, my_numbers))
            #print(my_winning_numbers)
            # points = 1 if len(my_winning_numbers) == 1 else 2 ** (len(my_winning_numbers) - 1) if len(my_winning_numbers) > 1 else 0

            points = 0
            if len(my_winning_numbers) == 1:
                points = 1
            if len(my_winning_numbers) > 1:
                points = 2 ** (len(my_winning_numbers)-1)

            total_points += points
            print(points)



    input_file.close()


if __name__ == '__main__':
    main()
    # main2()