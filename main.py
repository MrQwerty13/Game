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

selected = None

def draw_board(screen, board_data, selected):
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

            # highlight selected tile
            if selected == (x, y):
                pygame.draw.rect(screen, (255, 255, 255), rect, 3)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                mx, my = pygame.mouse.get_pos()
                grid_x, grid_y = mouse_to_grid((mx, my))

                if in_bounds(grid_x, grid_y):
                    selected = (grid_x, grid_y)
                print("Selected:", selected)

    screen.fill((0, 0, 0))

    draw_board(screen, game_board, selected)

    pygame.display.flip()
    clock.tick(CONSTS.FPS)

pygame.quit()