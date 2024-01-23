def parse_game_input(input_str):
    # Function to parse the input string into a dictionary representing the game
    game_data = {'id': None, 'cubes': []}

    # Split the input into game ID and cube subsets
    game_parts = input_str.split(':')

    # Extract game ID
    game_data['id'] = int(game_parts[0].strip().split()[1])

    # Extract cube subsets
    cubes_list = game_parts[1].strip().split(';')
    for subset in cubes_list:
        cubes = subset.strip().split(', ')
        game_data['cubes'].append({cube.split()[1]: int(cube.split()[0]) for cube in cubes})

    return game_data


def check_possible_games(games, red, green, blue):
    possible_games = []

    for game in games:
        valid_game = True

        for subset in game['cubes']:
            for color, count in subset.items():
                if color == 'red' and count > red:
                    valid_game = False
                elif color == 'green' and count > green:
                    valid_game = False
                elif color == 'blue' and count > blue:
                    valid_game = False

        if valid_game:
            possible_games.append(game['id'])

    return possible_games


def main():
    # Read the input file
    with open('input.txt', 'r') as file:
        input_data = file.read().splitlines()

    # Parse the input into game data
    games = [parse_game_input(line) for line in input_data]

    # Cube configuration
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    # Determine possible games
    possible_games = check_possible_games(games, red_cubes, green_cubes, blue_cubes)

    # Calculate the sum of IDs of possible games
    result = sum(possible_games)
    print("Sum of IDs of possible games:", result)


if __name__ == "__main__":
    main()
