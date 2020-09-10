import pygame,os
from pygame.locals import *
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
iteration = int(input('Enter iteration: '))  
length = int(input('Enter length of each segment: '))


thickness = int(input("How thick do you want your lines? "))

window = pygame.display.set_mode((0,0),RESIZABLE)
pygame.display.toggle_fullscreen
startx,starty = pygame.display.get_surface().get_size() 
startx /= 2
starty /= 2

r = 'r' 
l = 'l'
  
old = r 
new = old 

  

cycle = 1
  
totalCount = 0
while cycle<iteration: 
    
    new = (old) + (r)  
    
    old = old[::-1]  
    count = 0
    for char in range(0, len(old)):  
         
        if old[char] == r:  
             
            old = (old[:char])+ (l) + (old[char + 1:]) 
        
        elif old[char] == l:  
            
            old = (old[:char]) + (r) + (old[char + 1:])  
        print(str(count)+"/"+str(len(old))+" iterations of "+str(cycle)+" Complete")
        count += 1
    new = (new) + (old)  
  
    totalCount += count
    print("\n"*50+str(totalCount)+" Iterations completed.")
    old = new  
    """
    with open("Save",'a') as fish:
        fish.write("Generation "+str(cycle)+": "+new+'\n')
    """
    cycle = cycle + 1
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
    pygame.draw.line(window,(90,90,0),position,targetPos,thickness)
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
