import random
import CONSTS


GEM_TYPES = 4


def drop_down(board):
    for x in range(CONSTS.BOARD_WIDTH):
        column = []

        # собрать все НЕ None
        for y in range(CONSTS.BOARD_HEIGHT):
            if board[y][x] is not None:
                column.append(board[y][x])

        # сколько пустых сверху
        missing = CONSTS.BOARD_HEIGHT - len(column)

        # новые элементы сверху
        new_items = [
            random.randint(0, GEM_TYPES - 1)
            for _ in range(missing)
        ]

        column = new_items + column

        # записать обратно в board
        for y in range(CONSTS.BOARD_HEIGHT):
            board[y][x] = column[y]


def create_board():
    board = []

    for y in range(CONSTS.BOARD_HEIGHT):
        row = []
        for x in range(CONSTS.BOARD_WIDTH):
            gem = random.randint(0, GEM_TYPES - 1)
            row.append(gem)
        board.append(row)

    return board


def find_matches(board):
    matched = set()

    width = CONSTS.BOARD_WIDTH
    height = CONSTS.BOARD_HEIGHT

    # horizontal check
    for y in range(height):
        for x in range(width - 2):
            v = board[y][x]

            if v == board[y][x + 1] == board[y][x + 2]:
                matched.add((x, y))
                matched.add((x + 1, y))
                matched.add((x + 2, y))

    # vertical check
    for x in range(width):
        for y in range(height - 2):
            v = board[y][x]

            if v == board[y + 1][x] == board[y + 2][x]:
                matched.add((x, y))
                matched.add((x, y + 1))
                matched.add((x, y + 2))

    return matched

def remove_matches(board, matches):
    for x, y in matches:
        board[y][x] = None

def resolve_board(board):
    while True:
        matches = find_matches(board)

        if not matches:
            break

        remove_matches(board, matches)
        drop_down(board)