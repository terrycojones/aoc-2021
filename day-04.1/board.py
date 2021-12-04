class Board:
    def __init__(self):
        self.rows = []
        self.n = None

    def __str__(self):
        result = []
        for row in self.rows:
            result.append(' '.join(f'{number:2d}' for number in row))
        return '\n'.join(result)

    def addRow(self, row):
        numbers = list(map(int, row.split()))
        if self.n is None:
            self.n = len(numbers)
        else:
            assert len(numbers) == self.n
        self.rows.append(numbers)

    def call(self, number):
        for row in self.rows:
            for index, n in enumerate(row):
                if n == number:
                    row[index] = None
                    # Don't assume the number only occurs once.

    def bingo(self):
        for row in self.rows:
            if all(number is None for number in row):
                return True

        for index in range(self.n):
            col = [row[index] for row in self.rows]
            if all(number is None for number in col):
                return True

        return False

    def total(self):
        return sum(
            sum(
                0 if number is None else number
                for number in row
            ) for row in self.rows
        )


def readBoards(fp):
    boards = []
    board = None

    for line in fp:
        line = line.rstrip()
        if line:
            board.addRow(line)
        else:
            if board:
                boards.append(board)
            board = Board()

    if board:
        boards.append(board)

    return boards
