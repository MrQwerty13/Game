import pygame

import CONSTS
from Board import Board
from Colors import Colors


class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (
                CONSTS.SCREEN_WIDTH,
                CONSTS.SCREEN_HEIGHT
            )
        )

        pygame.display.set_caption(CONSTS.SCREEN_TITLE)

        self.clock = pygame.time.Clock()

        self.board = Board()

        self.running = True

        self.selected = None

        self.state = "idle"
        self.timer = 0

    # =====================================================
    # GAME LOOP
    # =====================================================

    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(CONSTS.FPS)

        pygame.quit()

    # =====================================================
    # INPUT
    # =====================================================

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
            ):
                self.handle_click(event.pos)

    def handle_click(self, pos):

        if self.state != "idle":
            return

        x = (
            pos[0] - CONSTS.BOARD_OFFSET_X
        ) // CONSTS.TILE_SIZE

        y = (
            pos[1] - CONSTS.BOARD_OFFSET_Y
        ) // CONSTS.TILE_SIZE

        if not (
            0 <= x < CONSTS.BOARD_WIDTH
            and
            0 <= y < CONSTS.BOARD_HEIGHT
        ):
            return

        if self.selected is None:

            self.selected = (x, y)
            return

        x1, y1 = self.selected
        x2, y2 = x, y

        if self.board.is_adjacent(
            x1,
            y1,
            x2,
            y2
        ):

            self.board.swap(
                x1,
                y1,
                x2,
                y2
            )

            matches = self.board.find_matches()

            if matches:

                self.board.resolve()

            else:

                self.board.swap(
                    x1,
                    y1,
                    x2,
                    y2
                )

        self.selected = None

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self):

        self.board.update()

    # =====================================================
    # DRAW
    # =====================================================

    def draw(self):

        self.screen.fill(CONSTS.BLACK)

        self.draw_board()

        pygame.display.flip()

    def draw_board(self):

        for row in self.board.cells:

            for cell in row:

                if cell is None:
                    continue

                pygame.draw.rect(
                    self.screen,
                    Colors.get_color(cell.value),
                    cell.get_rect()
                )

        if self.selected is not None:

            x, y = self.selected

            rect = pygame.Rect(
                CONSTS.BOARD_OFFSET_X + x * CONSTS.TILE_SIZE,
                CONSTS.BOARD_OFFSET_Y + y * CONSTS.TILE_SIZE,
                CONSTS.TILE_SIZE,
                CONSTS.TILE_SIZE
            )

            pygame.draw.rect(
                self.screen,
                CONSTS.WHITE,
                rect,
                3
            )