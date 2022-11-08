import pygame
from datetime import datetime
import pygame_menu 
from os import system
import button
import register
import pyautogui as pg


pygame.mixer.init()

class Display:
    w_init = 1/2
    h_init = 8/9
    angle = 0
    help_scale = (0.4,0.4) 
class Utillization:
    x = 0
    y = 1

def start_the_game():
    import mainGame
# game variables

gamesound = pygame.mixer.Sound("resource/sound/summer-by-lake-bird-chirping-01.mp3") # example sound
sound_on = False

pygame.init()
infoObject = pygame.display.Info()
size = [int(infoObject.current_w*Display.w_init),int(infoObject.current_h*Display.h_init)]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)

start_img = pygame.image.load('resource/image/start_btn.png').convert_alpha()
loginSubmit_button=button.Button(100,300,start_img,0.5)

email_box = button.InputBox(100, 100, 140, 32)
password_box = button.InputBox(100, 200, 140, 32)
input_boxes = [email_box,password_box]

def show_mode():
    menu.clear()
    menu.add.button('Game Start',start_the_game)
    menu.add.button('Back', back)
    menu.add.button('Quit', pygame_menu.events.EXIT)

def back():
    menu.clear()
    menu.add.button('Game Start', show_mode)
    menu.add.button('Help',show_help)
    menu.add.button('Quit', pygame_menu.events.EXIT)

def show_help():
    menu.clear()
    menu.add.button('Back',back)
    menu.add.image(image_path='resource/image/help_btn.png', angle=Display.angle, scale=Display.help_scale)


def sign_up():
    menu.clear()
    email=menu.add.text_input("email : ",id='email')
    password=menu.add.text_input("password : ",password=True,id='password')
    conFirmPassword=menu.add.text_input("conFirm password : ",password=True,id='password')
    menu.add.button('Submit',sign_up_button,email,password,conFirmPassword)

def sign_up_button(email,password,conFirmPassword):
    registerReturn=register.register(email.get_value(),password.get_value(),conFirmPassword.get_value())
    if registerReturn == 1:
        print(pg.alert(text='회원가입에 성공하셨습니다.', title='Next Dimension'))
    else:
        print(pg.alert(text='메일 입력을 다시 확인해주세요', title='Next Dimension'))



# 로그인
def login():
  menu.clear()
  email=menu.add.text_input("email : ",id='email')
  password=menu.add.text_input("password : ",password=True,id='password')
  menu.add.button('Submit',loginButton,email,password) #submit 버튼을 누르면 로그인 시도

def loginButton(email,password):
  login=register.Login(email.get_value(),password.get_value())
  if login!=0:
    print("로그인에 성공하셨습니다.") # 로그인 후 메인 화면으로 넘어갈 수 있게 해주세요!

def sound(sound):
    if sound==True:
        gamesound.play()

    else:
        gamesound.stop()

menu_image = pygame_menu.baseimage.BaseImage(image_path='resource/image/store_bg.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
mytheme = pygame_menu.themes.THEME_GREEN.copy()

mytheme.background_color = menu_image 
mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE

menu = pygame_menu.Menu('Next Dimension', size[Utillization.x], size[Utillization.y], theme=mytheme)
menu.add.button('Game Start',start_the_game)
menu.add.button('Help',show_help)
menu.add.button('Quit',pygame_menu.events.EXIT)
menu.add.button("login",login)
menu.add.button("register",sign_up)
menu.add.button("resetPassword",)
menu.add.toggle_switch("sound",True,sound)


background = pygame.image.load("resource/image/start_btn.png")



menu.mainloop(screen) 
pygame.quit()
