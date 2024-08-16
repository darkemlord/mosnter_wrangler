import pygame as pg


class Player(pg.sprite.Sprite):
    """Player class to control player character"""

    def __init__(self):
        """Initialize the player character"""
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(pg.Color("blue"))
        self.rect = self.image.get_rect()
        self.rect.center = (600, 350)
        self.speed = 5

    def update(self):
        """Update the player character"""
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed

    def warp(self):
        """Warp the player character to a random location"""
        pass

    def reset(self):
        """Reset the player character to the starting position"""
        pass
