class Dial:
    _position = 50

    def position(self):
        return self._position

    def position_after(self, move):
        direction = move[0]
        clicks = int(move[1:])

        if direction == 'R':
            self._position = (self._position + clicks) % 100
        else:  # direction L
            self._position = (self._position - clicks) % 100

        return self._position

    def position_after_moves_in_file(self, file):
        positions = []
        with open(file) as input_file:
            for move in input_file:
                positions.append(self.position_after(move))

        return positions

    def get_password(self, positions: list):
        password = 0
        for position in positions:
            if position == 0:
                password += 1

        return password


if __name__ == '__main__':
    dial = Dial()
    positions: list = dial.position_after_moves_in_file('input.txt')
    print(dial.get_password(positions))

# "Fast" TDD
#     dial = Dial()
#     assert dial.position() == 50
#     assert dial.position_after('R10') == 60
#     assert dial.position_after('L5') == 55
#     assert dial.position_after('R100') == 55
