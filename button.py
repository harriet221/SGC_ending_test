import pygame

# button class
class Button():
    def __init__(self, x, y, image, scale): # scale: 원래 scale배로 이미지 크기 조절
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        # mouse position
        pos = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # []: 0-left 1-middle 2-right mouse button
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0]==0: # mouse not clicked
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action