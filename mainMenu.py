import pygame
from datetime import datetime
import pygame_menu
from os import system
import button
import register
import pyautogui as pg
from register import db, firestore
import dataLoad

pygame.mixer.init()


class Display:
    w_init = 1/3
    h_init = 8/9
    angle = 0
    help_scale = (0.4, 0.4)
    arrowkey_scale = (0.1, 0.1)
    title_scale = (1, 1)


class Utillization:
    x = 0
    y = 1


def start_the_game():
    import mainGame


# game variables
gamesound = pygame.mixer.Sound(
    "resource/sound/summer-by-lake-bird-chirping-01.mp3")  # example sound
sound_on = False

pygame.init()
infoObject = pygame.display.Info()
size = [int(infoObject.current_w*Display.w_init),
        int(infoObject.current_h*Display.h_init)]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Next Dimension")  # 캡션

# 창이 resize되었는지 여부 체크


def on_resize() -> None:
    """
    Function checked if the window is resized.
    """
    window_size = screen.get_size()
    new_w, new_h = window_size[0], window_size[1]
    menu.resize(new_w, new_h)


# 회원가입 시 ID, PW 박스
email_box = button.InputBox(100, 100, 140, 32)
password_box = button.InputBox(100, 200, 140, 32)
input_boxes = [email_box, password_box]

# 로그인 전 보여지는 메뉴 화면(로그인, 회원가입)


def show_signinup():
    menu.clear()
    menu.add.image('resource/image/logo-silver.png',
                   angle=Display.angle, scale=Display.title_scale)
    menu.add.button('Sign in', login)
    menu.add.button('Sign up', sign_up)
    menu.add.button('Quit', pygame_menu.events.EXIT)

# 로그인 후 보여지는 메뉴 화면


def show_mode():
    menu.clear()
    menu.add.image('resource/image/logo-silver.png',
                   angle=Display.angle, scale=Display.title_scale)
    menu.add.button('Game Start', start_the_game)
    menu.add.button('Rank', rank)
    menu.add.button("Store", store)
    menu.add.button('Help', help)
    menu.add.button('About', about)
    menu.add.toggle_switch("Sound", True, sound)
    menu.add.button('Quit', pygame_menu.events.EXIT)


def rank():
    menu.clear()
    print("rank DB")  # 추후 Rank DB 생성되면 연결하기!
    menu.add.button('Back', show_mode)

# help 페이지


def help():
    menu.clear()
    menu.add.label('Story & Game Rule', font_size=35,
                   padding=(50, 0, 50, 0))  # about page title
    # story
    content = 'In 2300 AD, you can no longer live on Earth\n'\
        'and received a mission to find a new dimension for live.\n'\
        'Now you must find a new dimension\nwhile avoiding enemy attacks.\n'\
        'Good Luck!\n'
    menu.add.label(content, font_size=20)

    # game rule
    # key control
    menu.add.label(
        'Use left and right arrow key to move your character', font_size=20)
    # key images
    left_img = menu.add.image('resource/image/arrowkey_left.png',
                              angle=Display.angle, scale=Display.arrowkey_scale)
    right_img = menu.add.image('resource/image/arrowkey_right.png',
                               angle=Display.angle, scale=Display.arrowkey_scale)
    # key table
    table = menu.add.table(table_id='gamerule_key',
                           font_size=20, border_color=None, padding=(3, 1, 3, 1))
    table.add_row([left_img, '  Press left key to go left'])
    table.add_row([right_img, '  Press right key to go right'])

    # enemy HP detail
    menu.add.label('Enemies have different HPs', font_size=20)
    # enemy1 images
    enemy1_img1 = menu.add.image(
        'resource/image/chess_black_knight.png', angle=Display.angle, scale=Display.title_scale)
    enemy1_img2 = menu.add.image(
        'resource/image/green_bat.png', angle=Display.angle, scale=Display.title_scale)
    enemy1_img3 = menu.add.image(
        'resource/image/pirate_ship.png', angle=Display.angle, scale=Display.title_scale)
    enemy1_img4 = menu.add.image(
        'resource/image/card_jack.png', angle=Display.angle, scale=Display.title_scale)
    enemy1_img5 = menu.add.image(
        'resource/image/desert_snake.png', angle=Display.angle, scale=Display.title_scale)
    # enemy2 images
    enemy2_img1 = menu.add.image(
        'resource/image/chess_white_king.png', angle=Display.angle, scale=Display.title_scale)
    enemy2_img2 = menu.add.image(
        'resource/image/green_lizard.png', angle=Display.angle, scale=Display.title_scale)
    enemy2_img3 = menu.add.image(
        'resource/image/pirate_kraken.png', angle=Display.angle, scale=Display.title_scale)
    enemy2_img4 = menu.add.image(
        'resource/image/card_queen.png', angle=Display.angle, scale=Display.title_scale)
    enemy2_img5 = menu.add.image(
        'resource/image/desert_scolpion.png', angle=Display.angle, scale=Display.title_scale)
    # enemy table
    table2 = menu.add.table(table_id='gamerule_enemy', font_color='black', font_size=20, padding=(
        3, 1, 3, 1), background_color='white', border_width=0)
    table2.add_row([enemy1_img1, enemy1_img2, enemy1_img3,
                    enemy1_img4, enemy1_img5, '  Attack 1 time to kill'])
    table2.add_row([enemy2_img1, enemy2_img2, enemy2_img3,
                    enemy2_img4, enemy2_img5, '  Attack 2 times to kill'])
    menu.add.vertical_margin(100)
    menu.add.button('Back', show_mode)

# about 페이지


def about():
    menu.clear()
    menu.add.label('License & Source', font_size=35,
                   padding=(50, 0, 50, 0))  # about page title
    menu.add.label('Source', font_size=20)
    menu.add.url('https://github.com/Kill-Console/PythonShootGame',
                 'Kill-Console/PythonShootGame(The GPL License)', underline=False, font_color='white', font_size=18)
    menu.add.url('https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9',
                 'CSID-DGU/2021-2-OSSProj-PlusAlpha-9(The MIT License)', underline=False, font_color='white', font_size=18)
    menu.add.url('https://pixabay.com/ko/', 'pixabay',
                 font_color='white', underline=False, font_size=18)
    menu.add.url('https://www.soundeffectsplus.com/', 'soundeffectsplus',
                 underline=False, font_color='white', font_size=18)

    content = '\nCreated by\n'\
        'Dongguk University OSSProj\n'\
        'Seojeong Yun, Gaeun Lee, Seyeon Park'
    menu.add.label(content, font_size=20)

    menu.add.url('https://github.com/CSID-DGU/2022-2-OSSProj-SGC-3',
                 'Click here to go to our github link', font_color='white', font_size=20)
    menu.add.vertical_margin(100)
    menu.add.button('Back', show_mode)

# True가 반환될경우 소리가 켜지고 아니면 꺼짐


def sound(sound):
    if sound == True:
        gamesound.play()
    else:
        gamesound.stop()

# 회원가입 기능

def sign_up():
    menu.clear()
    email = menu.add.text_input("email : ", id='email')
    password = menu.add.text_input("password : ", password=True, id='password')
    menu.add.label(
        '* Please set the password to at least 8 digits', font_size=16)
    conFirmPassword = menu.add.text_input(
        "conFirm password : ", password=True, id='password')
    menu.add.button('Submit', sign_up_button, email, password, conFirmPassword)
    menu.add.button('Back', show_signinup)
# 회원가입 제출 버튼
def sign_up_button(email, password, conFirmPassword):
    registerReturn = register.register(
        email.get_value(), password.get_value(), conFirmPassword.get_value())
    if registerReturn == 1:
        print(pg.alert(text='회원가입에 성공하셨습니다.', title='Successfully signed up!'))
        show_mode()  # 메인 메뉴 페이지로 넘어가기
    else:
        print(pg.alert(text='메일 또는 비밀번호를 다시 확인해주세요.', title='sign up error'))

# 비밀번호 재설정 버튼


def resetPassword():
    menu.clear()
    email = menu.add.text_input("email : ", id='email')
    menu.add.button('Submit', resetPassword_Button, email)
    menu.add.button('Sign In', login)
    menu.add.button('Back', show_signinup)


def resetPassword_Button(email):
    register.passwordReset(email.get_value())
    print(pg.alert(text='메일을 통해 비밀번호를 재설정해주세요', title='Reset Password'))

def login():
    menu.clear()
    # 개발시 편의를 위해 default값 추가함 (추후 삭제 예정)
    email = menu.add.text_input(
        "Email : ", id='email', default='seyeon0627@gmail.com')
    password = menu.add.text_input("Password : ", password=True, id='password')
    menu.add.button('Submit', loginButton, email,
                    password)  # submit 버튼을 누르면 로그인 시도
    menu.add.button("Reset Password", resetPassword)
    menu.add.button('Back', show_signinup)


def loginButton(email, password):
    global user
    user = email.get_value()
    login = register.Login(email.get_value(), password.get_value())
    if login != 0:  # 로그인에 성공하면 다음으로 넘어감
        login_check = True
        #print(pg.alert(text='로그인에 성공하셨습니다.', title='Successfully signed in!'))
        show_mode()  # 메인 메뉴 페이지로 넘어가기
    else:
        print(pg.alert(text='메일 또는 비밀번호를 다시 확인해주세요.', title='sign in error'))


def resetPassword():
    menu.clear()
    email = menu.add.text_input("email : ", id='email')
    menu.add.button('Submit', resetPassword_Button, email)
    menu.add.button('Sign In', login)
    menu.add.button('Back', show_signinup)


def resetPassword_Button(email):
    register.passwordReset(email.get_value())
    print(pg.alert(text='메일을 통해 비밀번호를 재설정해주세요', title='Reset Password'))

# 로그인


def login():
    menu.clear()
    # 개발시 편의를 위해 default값 추가함 (추후 삭제 예정)
    email = menu.add.text_input(
        "Email : ", id='email', default='seyeon0627@gmail.com')
    password = menu.add.text_input("Password : ", password=True, id='password')
    menu.add.button('Submit', loginButton, email,
                    password)  # submit 버튼을 누르면 로그인 시도
    menu.add.button("Reset Password", resetPassword)
    menu.add.button('Back', show_signinup)


def loginButton(email, password):
    global user
    user=email.get_value()
    login=register.Login(email.get_value(),password.get_value())
    if login!=0: # 로그인에 성공하면 다음으로 넘어감
        #print(pg.alert(text='로그인에 성공하셨습니다.', title='Successfully signed in!'))
        show_mode() # 메인 메뉴 페이지로 넘어가기
    else:
        print(pg.alert(text='메일 또는 비밀번호를 다시 확인해주세요.', title='sign in error'))


def store():
    menu.clear()
    menu.add.label('Store', font_size=35, padding=(50, 0, 50, 0))  # page title
    menu.add.label("You Current coin") # 현재 코인 표시
    menu.add.label(dataLoad.coin_get(user))
    menu.add.label('Weapons')
    item_list=["bullets","missile","missile2","bomb"]
    buy_list = dataLoad.item_buyList_get(user)
    for item in item_list:
        if item in buy_list:
            image_path='resource/image/'+item+'_check.png'
            menu.add.image(image_path,
                        angle=Display.angle, scale=Display.help_scale)
            menu.add.button("Buy", Buy_check)
        else:
            image_path='resource/image/'+item+'_256px.png'
            menu.add.image(image_path,
                    angle=Display.angle, scale=Display.help_scale)
            menu.add.button("Buy", Buy, user,item)

    menu.add.vertical_margin(50)
    menu.add.button("Apply My Items", apply_item_page)
    menu.add.button('Back', show_mode)


def apply_item_page():

    menu.clear()
    buy_list = dataLoad.item_buyList_get(user)
    for item in buy_list:  # 사용자가 구매한 아이템 리스트 보여줌
        image_path = 'resource/image/'+item+"_256px.png"
        menu.add.image(image_path, angle=Display.angle,
                    scale=Display.help_scale)  # 구매한 아이템 이미지
        menu.add.button("Apply", apply_current_item,user,item)  # 아이템 적용 버튼

    menu.add.vertical_margin(50)
    menu.add.label("Current Applied item")
    item = dataLoad.item_apply_get(user)  # 현재 게임에 적용된 아이템 보여줌
    image_path = 'resource/image/'+item+"_256px.png"

    menu.add.image(image_path, angle=Display.angle, scale=Display.help_scale)

    menu.add.vertical_margin(50)
    menu.add.button("Back", store)



def Buy(user,item):
    dataLoad.item_buy(user,item)

def Buy_check():
    print(pg.alert(text='이미 구매한 아이템입니다.', title='Already Buy'))

def apply_current_item(user,item):
    dataLoad.item_apply(user,item)

# 여기서부터가 메인화면
menu_image = pygame_menu.baseimage.BaseImage(
    image_path='resource/image/background.jpg', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
mytheme = pygame_menu.themes.THEME_GREEN.copy()

mytheme.background_color = menu_image
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

# 첫 화면 페이지(로그인, 회원가입 버튼)
menu = pygame_menu.Menu(
    '', size[Utillization.x], size[Utillization.y], theme=mytheme)

if __name__ == '__main__':
    # 첫 화면 페이지(로그인, 회원가입 버튼)
    show_signinup() # 현재 로그인 되었는지 여부 확인. 로그인 되지 않았으면 show_signinup() 보여주기, 로그인 되었다면 show_mode() 보여주기!
    menu.enable()
    on_resize() # Set initial size
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                # Update the surface
                screen = pygame.display.set_mode((event.w, event.h),
                                                 pygame.RESIZABLE)
                # Call the menu event
                on_resize()

        menu.update(events)
        menu.draw(screen)

        pygame.display.flip()
        menu.mainloop(screen)
        pygame.quit()
else:
    size = [int(infoObject.current_w),
        int(infoObject.current_h)]
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    show_mode()
    menu.enable()
    on_resize() # Set initial size
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                # Update the surface
                screen = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                # Call the menu event
                on_resize()

        menu.update(events)
        menu.draw(screen)

        pygame.display.flip()
        menu.mainloop(screen)
        pygame.quit()
    
