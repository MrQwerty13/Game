import pygame
import CONSTS


class Cell:
    def __init__(self, value: int, grid_x: int, grid_y: int):
        self.value = value

        self.grid_x = grid_x
        self.grid_y = grid_y

        self.x = grid_x * CONSTS.TILE_SIZE
        self.y = grid_y * CONSTS.TILE_SIZE

        self.target_x = self.x
        self.target_y = self.y

        self.speed = 12
        self.is_moving = False

    def move_to(self, grid_x: int, grid_y: int):
        self.grid_x = grid_x
        self.grid_y = grid_y

        self.target_x = grid_x * CONSTS.TILE_SIZE
        self.target_y = grid_y * CONSTS.TILE_SIZE

        self.is_moving = True

    def update(self):
        if not self.is_moving:
            return

        if self.x < self.target_x:
            self.x = min(self.x + self.speed, self.target_x)
        elif self.x > self.target_x:
            self.x = max(self.x - self.speed, self.target_x)

        if self.y < self.target_y:
            self.y = min(self.y + self.speed, self.target_y)
        elif self.y > self.target_y:
            self.y = max(self.y - self.speed, self.target_y)

        if self.x == self.target_x and self.y == self.target_y:
            self.is_moving = False

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            CONSTS.TILE_SIZE,
            CONSTS.TILE_SIZE
        )