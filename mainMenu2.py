import pygame
from datetime import datetime
import pygame_menu 
from os import system
import button
import register
import pyautogui as pg
from register import db,firestore

pygame.mixer.init()

class Display:
    w_init = 1/3
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

# 회원가입 시 ID, PW 박스
email_box = button.InputBox(100, 100, 140, 32)
password_box = button.InputBox(100, 200, 140, 32)
input_boxes = [email_box,password_box]

def show_mode():
    menu.clear()
    menu.add.button('Game Start',start_the_game)
    menu.add.button('Help',show_help)
    menu.add.button('About',show_about)
    menu.add.button("Store",store)
    menu.add.toggle_switch("sound",True,sound)
    menu.add.button('Quit',pygame_menu.events.EXIT)

def back():
    menu.clear()
    menu.add.button('Game Start',start_the_game)
    menu.add.button('Help',show_help)
    menu.add.button('Quit',pygame_menu.events.EXIT)
    # menu.add.button("login",login)
    # menu.add.button("register",sign_up)
    # menu.add.button("resetPassword",resetPassword)
    menu.add.button("store",store)
    menu.add.toggle_switch("sound",True,sound)
    

def show_help():
    menu.clear()
    menu.add.image(image_path='resource/image/help_btn.png', angle=Display.angle, scale=Display.help_scale)
    menu.add.button('Back',back)

def show_about():
    menu.clear()
    menu.add.image(image_path='resource/image/help_btn.png', angle=Display.angle, scale=Display.help_scale)
    menu.add.button('Back',back)

#True가 반환될경우 소리가 켜지고 아니면 꺼짐
def sound(sound):
    if sound==True:
        gamesound.play()

    else:
        gamesound.stop()


# 회원가입 기능
def sign_up():
    menu.clear()
    email=menu.add.text_input("email : ",id='email')
    password=menu.add.text_input("password : ",password=True,id='password')
    conFirmPassword=menu.add.text_input("conFirm password : ",password=True,id='password')
    menu.add.button('Submit',sign_up_button,email,password,conFirmPassword)
    menu.add.button('Back',back)
#회원가입 제출 버튼
def sign_up_button(email,password,conFirmPassword):
    registerReturn=register.register(email.get_value(),password.get_value(),conFirmPassword.get_value())
    if registerReturn == 1:
        print(pg.alert(text='회원가입에 성공하셨습니다.', title='Next Dimension'))
    else:
        print(pg.alert(text='메일 입력을 다시 확인해주세요', title='Next Dimension'))
#비밀번호 재설정 버튼
def resetPassword():
    menu.clear()
    email=menu.add.text_input("email : ",id='email')
    menu.add.button('Submit',resetPassword_Button,email)

def resetPassword_Button(email):
    register.passwordReset(email.get_value())
    print(pg.alert(text='메일을 통해 비밀번호를 재설정 해주세요', title='Next Dimension'))

# 로그인
def login():
  menu.clear()
  email=menu.add.text_input("email : ",id='email')
  password=menu.add.text_input("password : ",password=True,id='password')
  menu.add.button('Submit',loginButton,email,password) #submit 버튼을 누르면 로그인 시도
  menu.add.button('home',back)

def loginButton(email,password):
    global user
    user=email.get_value()
    login=register.Login(email.get_value(),password.get_value())
    if login!=0: # 로그인에 성공하면 다음으로 넘어감
        print(pg.alert(text='로그인에 성공하셨습니다.', title='Next Dimension'))
        print("로그인에 성공하셨습니다.") # 로그인 후 메인 화면으로 넘어갈 수 있게 해주세요!
    


def store():
    menu.clear()
    menu.add.image('resource/image/bullets.png',angle=Display.angle, scale=Display.help_scale)
    menu.add.button("Buy",Buy,"bullets")
    menu.add.image('resource/image/missile.png',angle=Display.angle, scale=Display.help_scale)
    menu.add.button("Buy",Buy,"missile")
    menu.add.image('resource/image/missiles.png',angle=Display.angle, scale=Display.help_scale)
    menu.add.button("Buy",Buy,"missiles")
    menu.add.button('Back',back)


def Buy(item):
    db.collection("User").document(user).set({"item":firestore.ArrayUnion([item])})

# 여기서부터가 메인화면
menu_image = pygame_menu.baseimage.BaseImage(image_path='resource/image/store_bg.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
mytheme = pygame_menu.themes.THEME_GREEN.copy()

mytheme.background_color = menu_image 
mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE

menu = pygame_menu.Menu('Next Dimension', size[Utillization.x], size[Utillization.y], theme=mytheme)
show_mode() # 메인 메뉴 페이지


background = pygame.image.load("resource/image/start_btn.png")


menu.mainloop(screen) 
pygame.quit()
