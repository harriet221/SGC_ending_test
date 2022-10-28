# 게임의 메인 메뉴 페이지 ############################################################
# 뒤로가기, 소리on/off, 게임시작, 상점, 랭킹 확인, HELP, ABOUT 으로 연결되는 페이지 구성
#####################################################################################
import pygame

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

# button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self):
        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

# create button instances
start_button = Button(100,100,start_img)
exit_button = Button(100,200, exit_img)
back_button = Button(100,300, back_img)
rank_button = Button(100,400, rank_img)
help_button = Button(100,500, help_img)
about_button = Button(100,600, about_img)
sound_button = Button(100,700, sound_img)
store_button = Button(100,800, store_img)

# game loop
run = True
while run:

    # screen background
    screen.fill((202,228,214))
    start_button.draw()
    exit_button.draw()
    back_button.draw()
    rank_button.draw()
    help_button.draw()
    about_button.draw()
    sound_button.draw()
    store_button.draw()

    # event handler
    for event in pygame.event.get():

        # quit game(click upper right side x button)
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()