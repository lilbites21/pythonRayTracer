import pygame
import math
from Vectors import vector
from Surface import surface
from sunLight import sunLight
import Prims

WIDTH , HEIGHT = 400,400
FRAMERATE = 0.0001
BOUNCETIMES = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))

viewDistance = 1000

playerPos = vector(0,1,0)
lookingDir = vector(.3,0,0)


ball1Pos = vector(1,0,4)
ball1Radius = 1
ball1Surface = surface(pygame.Color(100,100,200),matalicness=.0,opacity=0)

ball2Pos = vector(.5,2,4)
ball2Radius = 1
ball2Surface = surface(pygame.Color(200,100,100),matalicness=.0,opacity=0)

plane1Pos = vector(0,-1.25,5)
plane1Normal = vector(0,1,0)
plane1Surface = surface(color=pygame.Color(0,255,0),matalicness=.1)

ball1 = Prims.sphere(ball1Pos,ball1Radius,name="ball",surface= ball1Surface)
ball2 = Prims.sphere(ball2Pos,ball2Radius, surface=ball2Surface)
plane1 = Prims.plane(center=plane1Pos,normal=plane1Normal,surface=plane1Surface,name= "plane 1")

sun = sunLight(vector(0,-1,0),2)

skySurface = surface((102,153,204))
skyColor = pygame.Color(102, 153, 204)

objects = [plane1,ball1,ball2]


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
            closenest = dist
        
    return closest



def getShade(normal:vector):
    #takes the dot product to the sun and shades on that
    colorScale:float = ((sun.dir)*(-1)) * normal
    colorScale *= sun.intencity
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
        colorScale = getShade(normal)
        objToSun = getObjectInDir(hitpoint,sun.dir*(-1))
        if objToSun == 0: #TODO cant get this to work, planes are actung up
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
    
    
