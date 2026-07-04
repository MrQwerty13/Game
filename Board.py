import random

import CONSTS
from Cell import Cell


class Board:
    GEM_TYPES = 4

    def __init__(self):
        self.cells = []
        self.create()

    def create(self):
        """Создать новое игровое поле."""
        self.cells.clear()

        for y in range(CONSTS.BOARD_HEIGHT):
            row = []

            for x in range(CONSTS.BOARD_WIDTH):
                value = random.randint(0, self.GEM_TYPES - 1)
                row.append(Cell(value, x, y))

            self.cells.append(row)

    def update(self):
        """Обновить анимацию всех клеток."""
        for row in self.cells:
            for cell in row:
                if cell is not None:
                    cell.update()

    def get_cell(self, x: int, y: int):
        return self.cells[y][x]

    def set_cell(self, x: int, y: int, cell):
        self.cells[y][x] = cell

    @staticmethod
    def is_adjacent(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2) == 1

    def swap(self, x1, y1, x2, y2):
        """Поменять местами две клетки."""
        self.cells[y1][x1], self.cells[y2][x2] = (
            self.cells[y2][x2],
            self.cells[y1][x1]
        )

        self.cells[y1][x1].move_to(x1, y1)
        self.cells[y2][x2].move_to(x2, y2)

    def find_matches(self):
        """Найти все совпадения 3+."""
        matches = set()

        # Горизонтальные
        for y in range(CONSTS.BOARD_HEIGHT):
            for x in range(CONSTS.BOARD_WIDTH - 2):

                c1 = self.cells[y][x]
                c2 = self.cells[y][x + 1]
                c3 = self.cells[y][x + 2]

                if (
                    c1 is not None
                    and c2 is not None
                    and c3 is not None
                    and c1.value == c2.value == c3.value
                ):
                    matches.update({
                        (x, y),
                        (x + 1, y),
                        (x + 2, y)
                    })

        # Вертикальные
        for x in range(CONSTS.BOARD_WIDTH):
            for y in range(CONSTS.BOARD_HEIGHT - 2):

                c1 = self.cells[y][x]
                c2 = self.cells[y + 1][x]
                c3 = self.cells[y + 2][x]

                if (
                    c1 is not None
                    and c2 is not None
                    and c3 is not None
                    and c1.value == c2.value == c3.value
                ):
                    matches.update({
                        (x, y),
                        (x, y + 1),
                        (x, y + 2)
                    })

        return matches

    def remove_matches(self, matches):
        """Удалить найденные совпадения."""
        for x, y in matches:
            self.cells[y][x] = None

    def drop_down(self):
        """Опустить все клетки вниз."""
        for x in range(CONSTS.BOARD_WIDTH):

            column = []

            for y in range(CONSTS.BOARD_HEIGHT):
                cell = self.cells[y][x]

                if cell is not None:
                    column.append(cell)

            missing = CONSTS.BOARD_HEIGHT - len(column)

            new_cells = []

            for y in range(missing):
                cell = Cell(
                    random.randint(0, self.GEM_TYPES - 1),
                    x,
                    y - missing
                )

                cell.move_to(x, y)

                new_cells.append(cell)

            column = new_cells + column

            for y, cell in enumerate(column):
                self.cells[y][x] = cell
                cell.move_to(x, y)

    def resolve(self):
        """Полностью обработать поле после удаления."""
        while True:

            matches = self.find_matches()

            if not matches:
                break

            self.remove_matches(matches)
            self.drop_down()