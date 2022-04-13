import pygame
import math

from Vectors import vector

import Scene

WIDTH , HEIGHT = 400,400
FRAMERATE = 0.0001
BOUNCETIMES = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))

viewDistance = 1000

playerPos = vector(0,5,0)
lookingDir = vector(1.4,0,0)


skyColor = pygame.Color(102, 153, 204)

objects,lights = Scene.get()
print(objects[0])


def addColor(col1:pygame.Color,col2:pygame.Color):
    if(type(col1) == tuple):
        col1 = pygame.Color(col1)
    if(type(col2) == tuple):
        col2 = pygame.Color(col2)
    r = min(255,(col1.r + col2.r))
    g = min(255,(col1.g + col2.g))
    b = min(255,(col1.b + col2.b))
    return pygame.Color(r,g,b)
def mulColor(col1:pygame.Color,num:float):
    if(type(col1) == tuple):
        r = int(min(255,(col1[0] * num)))
        g = int(min(255,(col1[1] * num)))
        b = int(min(255,(col1[2] * num)))
        return pygame.Color(r,g,b)
    r = int(min(255,(col1.r * num)))
    g = int(min(255,(col1.g * num)))
    b = int(min(255,(col1.b * num)))
    return pygame.Color(r,g,b)




def getObjectInDir(looking:vector,startPos:vector): 
    closest = 0
    closenest = viewDistance
    #goes through eich object to find what object it is
    for obj in objects:
        dist,hitpoint,normal = obj.getByRay(startPos,looking)
        if dist > 0 and (dist < closenest):
            closest = obj
            closenest = dist*1
        
    return closest



def getShade(normal:vector,hitpoint:vector):
    colorScale = 0
    if(hitpoint != 0):
        objToSun = getObjectInDir((lights[0].getDir(hitpoint)*(-1)),hitpoint)
        colorScale = ((lights[0].getDir(hitpoint)*(-1))*normal)
        colorScale *= lights[0].intencity
    #takes the dot product to the sun and shades on that
    if colorScale <= 0:
        return 0
    return colorScale



def rayColor(startRay:vector,times,startPos:vector):  

    startColor = pygame.Color(0,0,0) #later colors add to this
    thisObj = getObjectInDir(startRay,startPos)
    normal = 0
    hitpoint = 0
    dist:float = 0
    if(thisObj != 0):
        dist,hitpoint,normal = thisObj.getByRay(startPos,startRay)
    if(dist > 0):
        reflectRay = startRay - (normal*(startRay*normal))*2
        colorScale = getShade(normal,hitpoint)
        objToSun = getObjectInDir(hitpoint,lights[0].dir*(-1))
        #if objToSun == 0: #TODO cant get this to work, planes are acting up
        startColor = addColor(startColor,mulColor(mulColor(thisObj.surfaces.color,colorScale),1-thisObj.surfaces.matlicness))
        if(times > 0):
            startColor = startColor + mulColor(rayColor(reflectRay,times-1,hitpoint),thisObj.surfaces.matlicness)
        
        return startColor


    return skyColor



def rayObjects(x:int,y:int):
    #puts the ray comming out of that pixel
    sx = 2*x/WIDTH-1
    sy = 2*y/HEIGHT-1
    ray = vector(sx,sy,0)+vector(0,0,1)
    ray.normalize()
    ray = ray.rotateVector(lookingDir)
    
    colors = rayColor(ray,BOUNCETIMES,playerPos)
    return colors


def draw():
    #for each pixle call rayObjects
    for y in range(HEIGHT):
        for x in range(WIDTH):
            colorVal = rayObjects(x,HEIGHT - y)
            screen.set_at((x, y),colorVal)
        if y % 10 == 0:
            pygame.display.update()
    pygame.display.update()
    

def frame():
    draw()

if __name__ == "__main__":
    frame()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    
