import pygame as pg
import random


class Monster(pg.sprite.Sprite):
    """Monster class to control monster character"""

    def __init__(
        self,
        x: int,
        y: int,
        image: pg.Surface,
        monster_type,
        window_width: int,
        window_height: int,
    ):
        """Initialize the monster character"""
        super().__init__()
        self.window_width = (window_width,)
        self.window_height = window_height
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Monster type is an int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.type = monster_type

        # Set random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)

    def update(self):
        """Update the monster character"""
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity

        # Bounce the monster off the edges of the screen
        if self.rect.left < 0 or self.rect.right > self.window_width:
            self.dx *= -1 * self.dx
        if self.rect.top < 0 or self.rect.bottom > self.window_height:
            self.dy *= -1 * self.dy
