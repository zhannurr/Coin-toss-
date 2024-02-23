import pygame
import Settings
#  Кнопка
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        #  Позиция мыши
        pos = pygame.mouse.get_pos()

        # Проверка на клик мыши по кнопке
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                Settings.click_sound.play()

        #  Возвращаем переменную на False
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #  Вывести кнопку
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action