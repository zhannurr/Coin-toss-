import pygame
screen_height = 600
screen_width = 900
screen = pygame.display.set_mode((screen_width, screen_height))

image1 = pygame.image.load("images/image1.png")
image2 = pygame.image.load("images/image2.png")

pygame.mixer.init()

coin_flip_sound = pygame.mixer.Sound("audio/coinsound.wav")
stop_sound = pygame.mixer.Sound("audio/stop.wav")
click_sound = pygame.mixer.Sound("audio/click.wav")