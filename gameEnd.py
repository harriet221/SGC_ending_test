import pygame
import pygame_menu
# import mainMenu
import mainGame
import dataLoad
from register import user
from Defs import *

pygame.mixer.init()

# game variables
gamesound = pygame.mixer.Sound(Sounds.bird.value) # example sound
sound_on = False

pygame.init()
infoObject = pygame.display.Info()
size = [int(infoObject.current_w),int(infoObject.current_h)]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption(Content.main.value) # 캡션

# 창이 resize되었는지 여부 체크
def on_resize() -> None:
    window_size = screen.get_size()
    new_w, new_h = window_size[Utilization.x.value], window_size[Utilization.y.value]
    menu.resize(new_w, new_h)

# hidden 페이지 나타나기
def hidden():
    menu.clear()
    menu.add.button('OK',game_end)

# 스코어, 랭킹, restart, main 페이지 연결
score = mainGame.score
def game_end():
    menu.clear()
    menu.add.label(Content.end.value, font_size=Display.title_fontsize.value, padding=Display.padding_large.value)
    menu.add.label('Score: %d'%score) ## Defs.py에 저장
    menu.add.label('Rank: #1') # rank DB 연결 필요 # 추후 수정  ## Defs.py에 저장
    dataLoad.coin_set(user,score) # DB에 코인 저장 기능
    dataLoad.rank(user,score)
    menu.add.label('Total Coins: %d'%dataLoad.coin_get(user)) ## Defs.py 에 저장
    menu.add.vertical_margin(Display.small_margin.value)
    menu.add.button('Restart',start_the_game) # 수정
    menu.add.button('Main',start_the_mainMenu)
    menu.add.button('Quit',pygame_menu.events.EXIT)

def start_the_game():
    import mainGame

def start_the_mainMenu():
    from mainMenu import show_mode
    show_mode()


# 여기서부터가 메인화면
menu_image = pygame_menu.baseimage.BaseImage(image_path=Images.background.value,drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
mytheme = pygame_menu.themes.THEME_GREEN.copy()

mytheme.background_color = menu_image 
mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE

# 첫 화면 페이지(로그인, 회원가입 버튼)
menu = pygame_menu.Menu('', size[Utilization.x.value], size[Utilization.y.value], theme=mytheme)
hidden()
menu.enable()
on_resize() # Set initial size


if __name__ == '__main__':
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