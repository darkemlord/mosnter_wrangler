import pygame as pg


class Player(pg.sprite.Sprite):
    """Player class to control player character"""

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        """Initialize the player character"""
        super().__init__()
        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT
        self.image = pg.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pg.mixer.Sound("assets/catch.wav")
        self.die_sound = pg.mixer.Sound("assets/die.wav")
        self.warp_sound = pg.mixer.Sound("assets/warp.wav")

    def update(self):
        """Update the player character"""
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pg.K_RIGHT] and self.rect.right < self.window_width:
            self.rect.x += self.velocity
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocity
        if keys[pg.K_DOWN] and self.rect.bottom < self.window_height:
            self.rect.y += self.velocity

    def warp(self):
        """Warp the player character to a random location"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = self.window_height

    def reset(self):
        """Reset the player character to the starting position"""
        self.rect.centerx = self.window_width // 2
        self.bottom = self.window_height
