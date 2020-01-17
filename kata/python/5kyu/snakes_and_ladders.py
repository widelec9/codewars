class SnakesLadders:
    def __init__(self):
        self.board = [0,
                      0, 38, 0, 0, 0, 0, 14, 31, 0, 0,
                      0, 0, 0, 0, 26, 6, 0, 0, 0, 0,
                      42, 0, 0, 0, 0, 0, 0, 84, 0, 0,
                      0, 0, 0, 0, 0, 44, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 25, 0, 0, 11, 0,
                      67, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 19, 0, 60, 0, 0, 0, 0, 0, 0,
                      91, 0, 0, 53, 0, 0, 0, 98, 0, 0,
                      0, 0, 0, 0, 0, 0, 94, 0, 68, 0,
                      0, 88, 0, 0, 75, 0, 0, 0, 80, 0]
        self.player = 0
        self.square = [0, 0]
        self.game_over = False

    def play(self, die1, die2):
        if self.game_over:
            return 'Game over!'

        next_square = self.square[self.player] + die1 + die2
        if next_square <= 100:
            self.square[self.player] = self.square[self.player] + die1 + die2 if not self.board[next_square] else self.board[next_square]
        else:
            next_square = 200 - self.square[self.player] - die1 - die2
            self.square[self.player] = next_square if not self.board[next_square] else self.board[next_square]

        if self.square[self.player] == 100:
            self.game_over = True
            return 'Player {} Wins!'.format(int(self.player) + 1)

        if die1 != die2:
            self.player ^= 1
            return 'Player {} is on square {}'.format(int((self.player ^ 1) + 1), self.square[self.player ^ 1])
        return 'Player {} is on square {}'.format(int(self.player + 1), self.square[self.player])
