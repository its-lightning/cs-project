import cv2
import pygame
import time
import pyautogui

pygame.display.set_caption("Maze Runner")
#icon = pygame.image.load("")


screen = pygame.display.set_mode((1920,1080))

def menu_bg(mouse_x,mouse_y):
    move_menu_frame = pygame.image.load('New folder\menu main3.jpg')
    if (mouse_x > 1250 or mouse_x < 670 or mouse_y > 690 or mouse_y < 400) == True:
        if mouse_x > 1250 and mouse_y > 680:
            screen.blit(move_menu_frame,(0,0))
        elif mouse_x > 1250 and mouse_y < 400:
            screen.blit(move_menu_frame,(0,1080-800))
        elif mouse_x < 670 and mouse_y > 680:
            screen.blit(move_menu_frame,(1960-1390,0))
        elif mouse_x < 670 and mouse_y <400:
            screen.blit(move_menu_frame,(1960-1390,1080-800))
            
        elif mouse_x > 1250 :
            screen.blit(move_menu_frame,(0,1080-mouse_y-400))
        elif mouse_x < 670:
            screen.blit(move_menu_frame,(1960-1390,1080-mouse_y-400))
        elif mouse_y > 680:
            screen.blit(move_menu_frame,(1920-680-mouse_x,0))
        elif mouse_y < 400:
            screen.blit(move_menu_frame,(1920-680-mouse_x,1080-800))
            
    else:
        screen.blit(move_menu_frame,(1920-680-mouse_x,1080-mouse_y-400))
    

    
def menu():
    vidcap = cv2.VideoCapture('New folder\menu frame.mkv')
    
    '''while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
        frame_loaded,menu_frame = vidcap.read()
        if frame_loaded == True:
            menu_frame = cv2.cvtColor(menu_frame, cv2.COLOR_RGB2BGR)
            menu_frame = cv2.rotate(menu_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            menu_frame = cv2.flip(menu_frame, 0)
            menu_frame = pygame.pixelcopy.make_surface(menu_frame)
            screen.blit(menu_frame,(0,0))
            pygame.display.update()
        else:
            break'''

    screen_width, screen_height= pyautogui.size()
    pyautogui.moveTo(screen_width/2, screen_height/2)

    play = pygame.image.load('New folder\play.png')
    screen.blit(play,(884,508))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
        
        
        mouse_x,mouse_y = pygame.mouse.get_pos()
        menu_bg(mouse_x,mouse_y)

        print(mouse_x,mouse_y)
        if mouse_x < 1056 and mouse_x > 864 and mouse_y < 590 and mouse_y > 488:
            play = pygame.image.load('New folder\play.png')
            screen.blit(play,(700,508))
            pygame.display.update()
        else:
            play2 = pygame.image.load('New folder\play2.png')
            screen.blit(play2,(884,508))
            pygame.display.update()
        

        pygame.display.update()
        screen.fill((0,0,0))
        


whileno=0

while True:
    if whileno == 0:
        menu()
    

    whileno+=1







''' for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if pygame.key.get_pressed()[pygame.K_UP]:
            y-=10
            screen.blit(player,(x,y))
            pygame.display.update()
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            y+=10
            screen.blit(player,(x,y))
            pygame.display.update()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x-=10
            screen.blit(player,(x,y))
            pygame.display.update()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            x+=10
            screen.blit(player,(x,y))
            pygame.display.update()'''