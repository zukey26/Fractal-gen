from pygame.locals import RESIZABLE
import pygame
import json
import os

iterations = int(input("How many iterations? ")) - 1

width = 1400
height = 1000
length = 10
thickness = 1

r = "r"
l = "l"
new = list()

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


with open(f"save/{iterations}.json", "r") as fish:
    new = json.load(fish)["iterations"]


window = screen = pygame.display.set_mode((width, height))

window = pygame.display.set_mode((0,0),RESIZABLE)
pygame.display.toggle_fullscreen
startx,starty = pygame.display.get_surface().get_size() 
startx /= 2
starty /= 2

position = (startx,starty)
facing = 1
targetPos = (0,0)
for char in range(0, len(new)):
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        elif event.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.time.wait(1)
    if new[char] == (r):
        print("Right") 
        if facing == 1:# + y
            facing = 2
        elif facing == 2:# + x
            facing = 3
        elif facing == 3:# - y
            facing = 4
        elif facing == 4:# -x
            facing = 1
    elif new[char] == (l):     
        print("Left")
        if facing == 1:# + y
            facing = 4
        elif facing == 2:# + x
            facing = 1
        elif facing == 3:# - y
            facing = 2
        elif facing == 4:# -x
            facing = 3
    
    if facing == 1:
        targetPos = (position[0],position[1]+length)
    elif facing == 3:
        targetPos = (position[0],position[1]-length)
    elif facing == 2:
        targetPos = (position[0]+length,position[1])
    elif facing == 4:
        targetPos = (position[0]-length,position[1])
    print(position,targetPos)
    pygame.draw.line(window,(255,255,255),position,targetPos,thickness)
    position = targetPos



        
    pygame.display.flip()
done = False
while not done:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        elif event.type == pygame.QUIT:
            pygame.quit()
            done = True