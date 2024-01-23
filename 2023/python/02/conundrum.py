import re


def get_rgb(cubesets: list) -> list:
    max_red_cubes = 0
    max_green_cubes = 0
    max_blue_cubes = 0

    for cubeset in cubesets:
        cubes = int(re.search('\d+', cubeset).group())
        # color = re.search('[a-z]+', cubeset)

        if 'red' in cubeset and cubes > max_red_cubes:
            max_red_cubes = cubes
        elif 'green' in cubeset and cubes > max_green_cubes:
            max_green_cubes = cubes
        elif 'blue' in cubeset and cubes > max_blue_cubes:
            max_blue_cubes = cubes

    return [max_red_cubes, max_green_cubes, max_blue_cubes]


def is_valid_game(game, max_rgb):
    cubesets = game.rstrip().split(':')[1].replace(';', ',').split(',')
    rgb = get_rgb(cubesets)
    for i in range(len(max_rgb)):
        if rgb[i] > max_rgb[i]:
            return False
    return True


if __name__ == '__main__':
    input_file = open("input.txt", "r")

    sum = 0
    while True:
        game = input_file.readline()
        if not game:
            print("Sum: ", sum)
            break
        elif is_valid_game(game, [12, 13, 14]):
            game_id = int(game.strip().split(':')[0].split()[1])
            sum += game_id

    input_file.close()


