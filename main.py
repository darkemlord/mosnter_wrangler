import pygame as pg, random

# Initialize the game
pg.init()

# Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Monster Wrangler")

# Set frame rate
FPS = 60
clock = pg.time.Clock()

# main game loop
running = True
while running:
    # Check for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update the display
    pg.display.update()
    clock.tick(FPS)

# Quit the game
pg.quit()
