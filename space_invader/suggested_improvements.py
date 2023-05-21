import pygame
import random
import math
from pygame import mixer

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 64
ENEMY_SIZE = 64
NUMBER_OF_ENEMIES = 8
BOUNDARY_MARGIN = 64


class GameObject:
    def __init__(self, img_path, x, y):
        self.image = pygame.image.load(img_path)
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Player(GameObject):
    def __init__(self, img_path, x, y):
        super().__init__(img_path, x, y)
        self.dx = 0


class Enemy(GameObject):
    def __init__(self, img_path, x, y):
        super().__init__(img_path, x, y)
        self.dx = 0.5
        self.dy = 50


class Bullet(GameObject):
    def __init__(self, img_path, x, y):
        super().__init__(img_path, x, y)
        self.dy = 3
        self.is_visible = False

    def shoot(self, screen):
        self.is_visible = True
        screen.blit(self.image, (self.x + 16, self.y + 10))


def detect_collision(obj1, obj2):
    distance = math.hypot(obj1.x - obj2.x, obj1.y - obj2.y)
    return distance < 27


# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("./assets/Ufo.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("./assets/Background.jpg")

# Player
player = Player("./assets/Rocket.png", 368, 500)

# Enemies
enemies = [Enemy("./assets/enemy.png", random.randint(0, SCREEN_WIDTH - BOUNDARY_MARGIN), random.randint(50, 200)) for _
           in range(NUMBER_OF_ENEMIES)]

# Bullet
bullet = Bullet("./assets/bullet.png", 0, 500)

# Score
score = 0
my_font = pygame.font.Font('./assets/fastest.ttf', 32)

# End of game text
end_font = pygame.font.Font('./assets/fastest.ttf', 40)


def show_score():
    text = my_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))


def final_text():
    my_final_font = end_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(my_final_font, (200, 200))


# add music
mixer.music.load('./assets/background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Game loop
is_running = True
while is_running:
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.dx = -1
            elif event.key == pygame.K_RIGHT:
                player.dx = 1
            elif event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('./assets/shot.mp3')
                bullet_sound.play()
                if not bullet.is_visible:
                    bullet.x = player.x
                    bullet.shoot(screen)
        elif event.type == pygame.KEYUP:
            if event.key in {pygame.K_LEFT, pygame.K_RIGHT}:
                player.dx = 0

    player.x += player.dx
    player.x = max(0, min(player.x, SCREEN_WIDTH - BOUNDARY_MARGIN))

    for enemy in enemies:
        if enemy.y > 500:
            for enemy in enemies:
                enemy.y = 1000
            final_text()
            break

        enemy.x += enemy.dx

        if not 0 <= enemy.x <= SCREEN_WIDTH - BOUNDARY_MARGIN:
            enemy.dx *= -1
            enemy.y += enemy.dy

        if detect_collision(enemy, bullet):
            collision_sound = mixer.Sound('./assets/punch.mp3')
            collision_sound.play()
            bullet.y = 500
            bullet.is_visible = False
            score += 1
            enemy.x = random.randint(0, SCREEN_WIDTH - BOUNDARY_MARGIN)
            enemy.y = random.randint(50, 200)

        enemy.draw(screen)

    if bullet.y <= -64:
        bullet.y = 500
        bullet.is_visible = False
    if bullet.is_visible:
        bullet.shoot(screen)
        bullet.y -= bullet.dy

    player.draw(screen)
    show_score()

    pygame.display.update()

pygame.quit()
