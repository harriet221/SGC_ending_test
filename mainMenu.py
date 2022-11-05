# 게임의 메인 메뉴 페이지 ############################################################
# 뒤로가기, 소리on/off, 게임시작, 상점, 랭킹 확인, HELP, ABOUT 으로 연결되는 페이지 구성
#####################################################################################
import pygame
import button # button.py file
from button import InputBox 
import register


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

# caption
pygame.display.set_caption("Main Menu")

# text
font = pygame.font.SysFont('arialblack',40)
# text color
TEXT_COL = (255,255,255)
# text function
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

# game variables
menu_state = 'main'

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
store_button = button.Button(100,180, store_img, 0.5)
rank_button = button.Button(100,220, rank_img, 0.5)
help_button = button.Button(100,260, help_img, 0.5)
about_button = button.Button(100,300, about_img, 0.5)
sound_button = button.Button(100,340, sound_img, 0.5)
back_button = button.Button(100,380, back_img, 0.5)
loginSubmit_button=button.Button(100,500,start_img,0.5)


clock = pygame.time.Clock()

sign_in = False # 로그인 안된 상태
run = True 

email_box = InputBox(100, 100, 140, 32)
password_box = InputBox(100, 200, 140, 32)
input_boxes = [email_box,password_box]
sign_in = False

menu_state = 'main'

while not sign_in:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sign_in = True # 종료를 위한 임의 조치..?
            run=False
        for box in input_boxes:
            box.handle_event(event)


    for box in input_boxes:
        box.update()

    screen.fill((202,228,214))
    for box in input_boxes:
        box.draw(screen)
    if loginSubmit_button.draw(screen):
            login=register.Login(email_box.text,password_box.text)
            if(login!=0):
                sign_in=True
                


    pygame.display.flip()
    clock.tick(60)

menu_state = 'main'
# game loop
while run:

    # screen background
    screen.fill((202,228,214)) # background color

    # run buttons
    # check if the main menu is open
    if menu_state == 'main':
        if start_button.draw(screen):
            print('START') # test
            # play game page 연결
        if exit_button.draw(screen):
            run = False # close the window
        if rank_button.draw(screen):
            menu_state = 'rank'
        if help_button.draw(screen):
            menu_state = 'help'
        if about_button.draw(screen):
            menu_state = 'about'
        if sound_button.draw(screen):
            print('sound') # test
            # sound on/off 연결
        if store_button.draw(screen):
            menu_state = 'store'
    
    # check if the rank menu is open
    if menu_state == 'rank':
        # show rank (DB needed)
        if back_button.draw(screen):
            menu_state = 'main' # return to main menu
    
    # check if the help menu is open
    if menu_state == 'help':
        # show 게임 룰 설명
        if back_button.draw(screen):
            menu_state = 'main'
    
    # check if the about menu is open
    if menu_state == 'about':
        # show 라이선스, 제작자
        if back_button.draw(screen):
            menu_state = 'main'
    
    # check if the store menu is open
    if menu_state == 'store':
        # store page 연결
        draw_text("STORE",font,TEXT_COL,160,260)
        if back_button.draw(screen):
            menu_state = 'main'

    

    # event handler
    for event in pygame.event.get():

        # quit game(when click upper right side 'x' button)
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()


pygame.quit()