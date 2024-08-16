import pygame as pg


class Monster(pg.sprite.Sprite):
    """Monster class to control monster character"""

    def __init__(self):
        """Initialize the monster character"""
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(pg.Color("red"))
        self.rect = self.image.get_rect()
        self.rect.center = (600, 350)
        self.speed = 5

    def update(self):
        """Update the monster character"""
        pass
