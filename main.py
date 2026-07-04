import pygame

import CONSTS
import board
from colors import get_color


pygame.init()

screen = pygame.display.set_mode(
    (CONSTS.SCREEN_WIDTH, CONSTS.SCREEN_HEIGHT)
)

pygame.display.set_caption(CONSTS.SCREEN_TITLE)

clock = pygame.time.Clock()

game_board = board.create_board()


def mouse_to_grid(pos):
    x, y = pos
    return x // CONSTS.TILE_SIZE, y // CONSTS.TILE_SIZE


def in_bounds(x, y):
    return (
        0 <= x < CONSTS.BOARD_WIDTH and
        0 <= y < CONSTS.BOARD_HEIGHT
    )


def swap(board_data, x1, y1, x2, y2):
    board_data[y1][x1], board_data[y2][x2] = board_data[y2][x2], board_data[y1][x1]


def is_adjacent(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2) == 1


def draw_board(screen, board_data, selected, matches=None):
    for y in range(len(board_data)):
        for x in range(len(board_data[y])):
            value = board_data[y][x]

            color = get_color(value)

            rect = pygame.Rect(
                x * CONSTS.TILE_SIZE,
                y * CONSTS.TILE_SIZE,
                CONSTS.TILE_SIZE,
                CONSTS.TILE_SIZE
            )

            pygame.draw.rect(screen, color, rect)

            # selected highlight
            if selected == (x, y):
                pygame.draw.rect(screen, (255, 255, 255), rect, 3)

            # matches highlight
            if matches and (x, y) in matches:
                pygame.draw.rect(screen, (255, 255, 255), rect, 4)


selected = None
matches = set()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                grid_x, grid_y = mouse_to_grid((mx, my))

                if not in_bounds(grid_x, grid_y):
                    continue

                if selected is None:
                    selected = (grid_x, grid_y)
                else:
                    x1, y1 = selected
                    x2, y2 = grid_x, grid_y

                    if is_adjacent(x1, y1, x2, y2):
                        swap(game_board, x1, y1, x2, y2)

                    selected = None

    # обновление матчей (ВАЖНО: каждый кадр)
    matches = board.find_matches(game_board)

    screen.fill((0, 0, 0))

    draw_board(screen, game_board, selected, matches)

    pygame.display.flip()
    clock.tick(CONSTS.FPS)

pygame.quit()