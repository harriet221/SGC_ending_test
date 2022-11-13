import pygame
import pygame_menu

pygame.mixer.init()

class Display:
    w_init = 1
    h_init = 1
    angle = 0
    help_scale = (0.4,0.4)
    arrowkey_scale = (0.1,0.1)
    title_scale=(1,1)
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
pygame.display.set_caption("Next Dimension") # 캡션

# 창이 resize되었는지 여부 체크
def on_resize() -> None:
    """
    Function checked if the window is resized.
    """
    window_size = screen.get_size()
    new_w, new_h = window_size[0], window_size[1]
    menu.resize(new_w, new_h)

# 게임 end 페이지
def game_end():
    menu.clear()
    menu.add.label('Game End', font_size=35,padding=(50,0,50,0))

# 여기서부터가 메인화면
menu_image = pygame_menu.baseimage.BaseImage(image_path='resource/image/background.jpg',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
mytheme = pygame_menu.themes.THEME_GREEN.copy()

mytheme.background_color = menu_image 
mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE

# 첫 화면 페이지(로그인, 회원가입 버튼)
menu = pygame_menu.Menu('', size[Utillization.x], size[Utillization.y], theme=mytheme)
game_end()
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