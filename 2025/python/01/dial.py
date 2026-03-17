class Dial:
    _position = 50

    def position(self):
        return self._position

    def position_after(self, n):
        direction = n[0]
        clicks = int(n[1:])
        if direction == 'R':
            self._position += clicks
        else:
            self._position -= clicks
        return self._position


if __name__ == '__main__':
    dial = Dial()
    assert dial.position() == 50
    assert dial.position_after('R10') == 60
    assert dial.position_after('L5') == 55
    assert dial.position_after('R100') == 55
