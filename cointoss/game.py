import pygame
import random
import pygame_menu
import sys
from pygame_menu import themes
from Button import Button
from Coin import Coin
from Settings import *

pygame.init()

pygame.font.init()
font_1 = pygame.font.SysFont('MS Gothic', 40)
font_2 = pygame.font.SysFont('MS Gothic', 50)
font_3 = pygame.font.SysFont('MS PGothic',55, True)

pygame.display.set_caption("Coin Toss Simulator")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

orel_btn_img = pygame.image.load("images/orelbtn.png").convert_alpha()
orel_btn_img = pygame.transform.scale(orel_btn_img, (200, 200))

reshka_btn_img = pygame.image.load("images/reshkabtn.png").convert_alpha()
reshka_btn_img = pygame.transform.scale(reshka_btn_img, (200, 200))

restart_btn_img = pygame.image.load("images/restartbtn.png").convert_alpha()
restart_btn_img = pygame.transform.scale(restart_btn_img, (66, 66))

menu_btn_img = pygame.image.load("images/menubtn.png").convert_alpha()
menu_btn_img = pygame.transform.scale(menu_btn_img, (50, 50))

#  Кнопки
orel_button = Button(screen_width // 2 - 250, screen_height // 2 - 100, orel_btn_img, 1)
reshka_button = Button(screen_width // 2 + 50, screen_height // 2 - 100, reshka_btn_img, 1)
restart_button = Button(screen_width // 2 - 40, screen_height // 2 - 66, restart_btn_img, 1)
menu_button = Button(850, 0, menu_btn_img, 1)


def result_check(guess, result):
    if guess == result:
        draw_text("You are correct", font_1, (6, 47, 70), 320, 180)
        return True
    else:
        draw_text("You are wrong", font_1, (6, 47, 70), 320, 180)
        return False

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


def play(game_rounds, total_chances):
    chances = total_chances
    counter = 0
    choosing = True
    guess = 0
    clock = pygame.time.Clock()
    main_coin = Coin((screen_width / 2) - 64, (screen_height / 2) - 120)

    rand = random.randint(1, 2)
    if rand == 1:
        result = "HEAD"
    else:
        result = "TAIL"
    show_result = False
    run = True
    is_win = False
    counted_this_round = False

    WIN_GAME = False

    FPS = 60
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return


        if choosing:
            counted_this_round = False
            chances_this_round = False
            screen.fill(("powder blue"))

            if orel_button.draw(screen):
                guess = 'HEAD'
                choosing = False
            if reshka_button.draw(screen):
                guess = 'TAIL'
                choosing = False
        else:

            if not chances_this_round:
                chances -= 1
                chances_this_round = True
            if result == guess and not counted_this_round:
                counter += 1
                counted_this_round = True

            if main_coin.frames > 1:  # пока идет анимация
                screen.fill(("powder blue"))
                draw_text(f'Your choice is {guess}', font_1, (6, 47, 70), 10, 10)
                main_coin.update()


            else:
                screen.fill(("powder blue"))

                draw_text(f"Score:{counter}/{game_rounds}", font_1, (6, 47, 70), 700, 500)
                draw_text(f"Chances:{chances}/{total_chances}", font_1, (6, 47, 70), 670, 560)

                draw_text(f'{result}', font_2, (6, 47, 70), 395, 100)
                draw_text(f'Your choice is {guess}', font_1, (6, 47, 70), 10, 10)

                if result == 'HEAD':
                    screen.blit(image1, ((screen_width / 2) - 64, (screen_height / 2) + 50))

                elif result == 'TAIL':
                    screen.blit(image2, ((screen_width / 2) - 64, (screen_height / 2) + 50))

                if game_rounds == counter:
                    draw_text("YOU WIN",font_3,((218, 165, 32)), screen_width//2-100, screen_height//2 )
                    WIN_GAME = True

                is_win = result_check(guess, result)

                if chances == 0 and WIN_GAME == False:
                    draw_text("YOU LOSE", font_3, (218, 165, 32), screen_width // 2-100, screen_height // 2)
                    chances = total_chances

                if menu_button.draw(screen):
                    run = False
                    
                if restart_button.draw(screen):
                    choosing = True
                    counted_this_round = False
                    main_coin.frames = 200  # зановоо начинается
                    rand = random.randint(1, 2)
                    if rand == 1:
                        result = "HEAD"
                    else:
                        result = "TAIL"
                    if WIN_GAME == True:
                        chances = total_chances
                        WIN_GAME = False
                        counter = 0

        pygame.display.flip()
        clock.tick(FPS)

def start_game_easy():
    click_sound.play()
    mainmenu.disable()
    play(1,3)
def start_game_medium():
    click_sound.play()
    mainmenu.disable()
    play(3,5)
def start_game_hard():
    click_sound.play()
    mainmenu.disable()
    play(5,7)
def dark_theme():
    global mainmenu
    global diff

    if mainmenu.get_theme() != themes.THEME_DARK:
        click_sound.play()

        theme = themes.THEME_DARK
        if diff.get_theme()!= themes.THEME_DARK:
            theme = themes.THEME_DARK

    else:
        click_sound.play()

        theme = themes.THEME_DARK

    mainmenu.clear()

    mainmenu = pygame_menu.Menu('Main menu', screen_width, screen_height, theme=theme)
    diff = pygame_menu.Menu('Difficulty', screen_width, screen_height, theme=theme)

    display_menu(mainmenu)
    mainmenu.mainloop(screen)

def blue_theme():
    global mainmenu
    global diff
    if mainmenu.get_theme() != themes.THEME_BLUE:
        click_sound.play()

        theme = themes.THEME_BLUE
        if diff.get_theme() != themes.THEME_BLUE:
            theme = themes.THEME_BLUE
    else:
        click_sound.play()

        theme = themes.THEME_BLUE
    mainmenu.clear()

    mainmenu = pygame_menu.Menu('Main menu', screen_width, screen_height, theme=theme)
    diff = pygame_menu.Menu('Difficulty', screen_width, screen_height, theme=theme)

    display_menu(mainmenu)

def display_menu(mainmenu):
    diff = pygame_menu.Menu("Difficulty menu", screen_width, screen_height, theme=themes.THEME_BLUE)
    diff.add.button("Easy", start_game_easy)
    diff.add.button("Medium", start_game_medium)
    diff.add.button("Hard", start_game_hard)
    mainmenu.add.button('PLAY', diff)
    mainmenu.add.button('Dark Theme', dark_theme)
    mainmenu.add.button('Light Theme', blue_theme)
    mainmenu.add.button('Quit', pygame_menu.events.EXIT)
    mainmenu.mainloop(screen)

mainmenu = pygame_menu.Menu('Main menu', screen_width, screen_height, theme=themes.THEME_BLUE)
diff = pygame_menu.Menu("Difficulty menu", screen_width, screen_height, theme=themes.THEME_BLUE)

display_menu(mainmenu)
pygame.quit()
