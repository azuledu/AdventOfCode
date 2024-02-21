import re


def get_fewest_rgb(game: str) -> list:
    min_red_cubes = 0
    min_green_cubes = 0
    min_blue_cubes = 0

    cubesets = game.rstrip().split(':')[1].replace(';', ',').split(',')

    for cubeset in cubesets:
        cubes = int(re.search('\d+', cubeset).group())
        # color = re.search('[a-z]+', cubeset)

        if 'red' in cubeset and cubes > min_red_cubes:
            min_red_cubes = cubes
        elif 'green' in cubeset and cubes > min_green_cubes:
            min_green_cubes = cubes
        elif 'blue' in cubeset and cubes > min_blue_cubes:
            min_blue_cubes = cubes

    return [min_red_cubes, min_green_cubes, min_blue_cubes]


def is_valid_game(game, max_rgb):
    rgb = get_fewest_rgb(game)
    for i in range(len(max_rgb)):
        if rgb[i] > max_rgb[i]:
            return False
    return True


def main():
    input_file = open("input.txt", "r")

    max_rgb = [12, 13, 14]
    sum_of_ids = 0
    sum_of_powers = 0
    while True:
        game = input_file.readline()
        if not game:
            print("Sum of IDs: ", sum_of_ids)
            print("Sum of powers: ", sum_of_powers)
            break
        elif is_valid_game(game, max_rgb):
            game_id = int(game.strip().split(':')[0].split()[1])
            sum_of_ids += game_id

        power = 1
        fewest_rgb = get_fewest_rgb(game)
        for min_cubes in fewest_rgb:
            power *= min_cubes
        sum_of_powers += power

    input_file.close()


if __name__ == '__main__':
    main()



