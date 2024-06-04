# Pygame Project 
# Author: Joy Dong
# May 28, 2024

import pygame as pg
import random

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 900  # Pixels
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/batman.webp")
        self.rect = self.image.get_rect()

        self.image = pg.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.rect = self.image.get_rect()

        self.lives = 3

    def update(self):

        # Update the location
        # Controlled by the mouse

        self.rect.center = pg.mouse.get_pos()

        # Keep at the bottom of the screen

        if self.rect.top < HEIGHT -200:
            self.rect.top = HEIGHT - 200

class Book(pg.sprite.Sprite):
    def __init__(self, size: int):
        super().__init__()

        # Book appearance
        self.image = pg.Surface((size, size))
        pg.draw.circle(self.image, WHITE, (size // 2, size //2),  size // 2)
        
        self.rect = self.image.get_rect()

        # Spawn book at the top of the screen

        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = HEIGHT

        self.vel_y = 6

    def update(self):
        # Movement
        self.rect.y += self.vel_y

        if self.rect.bottom >= HEIGHT + 10:
            self.rect.y = -10

        # Kill if it hits the floor
        if self.rect.bottom < 0:
            self.kill()

        # And lose a life


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()


    # 1) From George's Jungle Jam
    # Falling time
    book_fallen = 900
    last_book_fallen = pg.time.get_ticks()

    # 2) From George's Jungle Jam
    # Difficulty
    difficulty = 0


    #Score
    score = 0

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    book_sprites = pg.sprite.Group()

    player = Player()
    all_sprites.add(player)

    pg.display.set_caption("<WINDOW TITLE HERE>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state

        all_sprites.update()


        books_collided = pg.sprite.spritecollide(player, book_sprites, True)

        for book in books_collided:
            # Increase the score by 1
            score += 1
            print(f"Score: {score}")

        # 3) From George's Jungle Jam
        if pg.time.get_ticks() > last_book_fallen + book_fallen:
            last_book_fallen = pg.time.get_ticks()
            book = Book(10)
            all_sprites.add(book)
            book_sprites.add(book)

        # 4) From George's Jungle Jam
        # Increase speed 
        if score  >= difficulty:
            book_fallen-= 50
            difficulty += 10


    



        # CHANGE THIS TO COLLIDING WITH THE FLOOR!

        # book_collided = pg.sprite.spritecollide(player, book_sprites, False)

        # for book in book_collided:
        #     player.lives -= 0.1 
        #     print(int(player.lives))


        # --- Draw items
        screen.fill(BLACK)

        # Draw all of the sprites
        
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()
if __name__ == "__main__":
    main()