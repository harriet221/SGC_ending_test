# 게임의 메인 메뉴 페이지 ############################################################
# 뒤로가기, 소리on/off, 게임시작, 상점, 랭킹 확인, HELP, ABOUT 으로 연결되는 페이지 구성
#####################################################################################
import pygame
import button # button.py file

pygame.init()

# create game window
class Display:
    w_init = 1/3
    h_init = 7/9
    angle = 0
    help_scale = (0.4,0.4) 
class Utillization:
    x = 0
    y = 1

infoObject = pygame.display.Info()
size = [int(infoObject.current_w*Display.w_init),int(infoObject.current_h*Display.h_init)]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)

pygame.display.set_caption("Main Menu")

# load button images
start_img = pygame.image.load('resource/image/start_btn.png').convert_alpha()
exit_img = pygame.image.load('resource/image/exit_btn.png').convert_alpha()
back_img = pygame.image.load('resource/image/back_btn.png').convert_alpha()
rank_img = pygame.image.load('resource/image/rank_btn.png').convert_alpha()
help_img = pygame.image.load('resource/image/help_btn.png').convert_alpha()
about_img = pygame.image.load('resource/image/about_btn.png').convert_alpha()
sound_img = pygame.image.load('resource/image/sound_btn.png').convert_alpha()
store_img = pygame.image.load('resource/image/store_btn.png').convert_alpha()

# create button instances
start_button = button.Button(100,100,start_img, 0.5) # start point x, y, image, scale
exit_button = button.Button(100,140, exit_img, 0.5)
back_button = button.Button(100,180, back_img, 0.5)
rank_button = button.Button(100,220, rank_img, 0.5)
help_button = button.Button(100,260, help_img, 0.5)
about_button = button.Button(100,300, about_img, 0.5)
sound_button = button.Button(100,340, sound_img, 0.5)
store_button = button.Button(100,380, store_img, 0.5)

# game loop
run = True
while run:

    # screen background
    screen.fill((202,228,214)) # background color

    # button run
    if start_button.draw(screen):
        print('START') # test
    if exit_button.draw(screen):
        print('exit') # test
        run = False # close the window
    if back_button.draw(screen):
        print('back') # test
    if rank_button.draw(screen):
        print('rank') # test
    if help_button.draw(screen):
        print('help') # test
    if about_button.draw(screen):
        print('about') # test
    if sound_button.draw(screen):
        print('sound') # test
    if store_button.draw(screen):
        print('store') # test

    # event handler
    for event in pygame.event.get():

        # quit game(when click upper right side 'x' button)
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()