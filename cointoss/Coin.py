from Settings import *

screen_height = 600
screen_width = 900

COIN_WIDTH = 128
COIN_HEIGHT = 128
image1 = pygame.image.load("images/image1.png")
image2 = pygame.image.load("images/image2.png")
images = (image1, image2)


class Coin:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.image = image1
        self.coin_velocity = 0
        self.gravity = 1
        self.jump_strength = -25

        self.rect = pygame.Rect(x, y, COIN_WIDTH, COIN_HEIGHT)
        self.frames = 180

    def update(self):
        if self.frames > 1:  # пока идет анимация


            self.coin_velocity += self.gravity
            self.y += self.coin_velocity

            if self.y <= 0:  # Check if coin reaches the top
                self.coin_velocity = 0  # Stop the coin at the top
                coin_flip_sound.stop()  # Stop coin flip sound

            if self.y >= screen_height - self.rect.y:
                self.y = screen_height - self.rect.y
                self.coin_velocity = self.jump_strength
                coin_flip_sound.play(0)
                if self.image == image1:
                    self.image = image2
                else:
                    self.image = image1
            self.display_coin()
            self.frames -= 1
        if self.frames == 2:
            stop_sound.play(0)
    def display_coin(self):
        screen.blit(self.image, (self.x, self.y))