import random
import CONSTS


GEM_TYPES = 4


def create_board():
    board = []

    for y in range(CONSTS.BOARD_HEIGHT):
        row = []
        for x in range(CONSTS.BOARD_WIDTH):
            gem = random.randint(0, GEM_TYPES - 1)
            row.append(gem)
        board.append(row)

    return board