import pygame as pg
import random


class Game:
    """Game class to control game play"""

    def __init__(
        self,
        player,
        monster_group,
        window_width: int,
        window_height: int,
        fps: int,
        display_surface: pg.Surface,
    ):
        """Initialize the game"""
        # Set game values
        self.score = 0
        self.round_number = 0
        self.round_time = 0
        self.frame_count = 0
        self.player = player
        self.monster_group = monster_group
        self.fps = fps
        self.window_width = window_width
        self.window_height = window_height
        self.display_surface = display_surface

        # Set game sounds

        self.next_level_sound = pg.mixer.Sound("assets/next_level.wav")

        # Set game fonts
        self.font = pg.font.Font("assets/Abrushow.ttf", 24)

        # Set images
        blue_image = pg.image.load("assets/blue_monster.png")
        green_image = pg.image.load("assets/green_monster.png")
        purple_image = pg.image.load("assets/purple_monster.png")
        yellow_image = pg.image.load("assets/yellow_monster.png")

        # This list corresponds to the monster types int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.target_monster_images = [
            blue_image,
            green_image,
            purple_image,
            yellow_image,
        ]

        self.target_monster_type = random.randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = window_width // 2
        self.target_monster_rect.top = 30

    def update(self):
        """Update the game objects"""
        self.frame_count += 1
        if self.frame_count == self.fps:
            self.round_time += 1
            self.frame_count = 0

        self.check_collisions()

    def draw(self):
        """Draw the game objects"""
        # Set Colors
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        PURPLE = (128, 0, 128)
        YELLOW = (255, 255, 0)

        # Add the monster colors to a list where the index corresponds to the monster type
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        # set text
        catch_text = self.font.render("Current catch ", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = self.window_width // 2
        catch_rect.top = 5

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        lives_text = self.font.render(f"Lives: {self.player.lives}", True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        round_text = self.font.render(f"Round: {self.round_number}", True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

        time_text = self.font.render(f"Time: {self.round_time}", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (self.window_width - 10, 5)

        warp_text = self.font.render(f"Warps: {self.player.warps}", True, WHITE)
        warp_text_rect = warp_text.get_rect()
        warp_text_rect.topright = (self.window_width - 10, 35)

        # Blit the HUD
        self.display_surface.blit(catch_text, catch_rect)
        self.display_surface.blit(score_text, score_rect)
        self.display_surface.blit(round_text, round_rect)
        self.display_surface.blit(lives_text, lives_rect)
        self.display_surface.blit(time_text, time_rect)
        self.display_surface.blit(warp_text, warp_text_rect)
        self.display_surface.blit(self.target_monster_image, self.target_monster_rect)

        pg.draw.rect(
            self.display_surface,
            colors[self.target_monster_type],
            (self.window_width // 2 - 32, 30, 64, 64),
            2,
        )

        pg.draw.rect(
            self.display_surface,
            colors[self.target_monster_type],
            (0, 100, self.window_width, self.window_height - 200),
            4,
        )

    def check_collisions(self):
        """Check for collisions between game objects"""
        # Check for collision between a player and an individual monster
        # We must test the type of the monster to see if it matches the type of our target monster
        collided_monster = pg.sprite.spritecollideany(self.player, self.monster_group)

        # we collider with a monster
        if collided_monster:
            # Caught the correct monster
            if collided_monster.type == self.target_monster_type:
                self.score += 100 * self.round_number
                # remove caught monster
                collided_monster.remove(self.monster_group)
                if self.monster_group:
                    # there are more monsters to catch
                    self.player.catch_sound.play()
                    self.choose_new_target()
                else:
                    # The round is over
                    self.player.reset()
                    self.start_new_round()

    def start_new_round(self):
        """Start a new round of the game"""
        # Provide a score bonus based on how quickly the player caught the monster
        self.score += int(10000 * self.round_number / (1 + self.round_time))

        # Reset round values
        self.round_time = 0
        self.frame_count = 0
        self.round_number += 1
        self.player.warps += 1

    def choose_new_target(self):
        """Choose a new target for the player"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass
