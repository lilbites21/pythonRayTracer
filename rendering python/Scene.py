from Vectors import vector
from Surface import surface
from pygame import Color
from PIL import Image

import Light
import Prims

def getNormalInfo(normalImage,scale = [1,1]):
    pixels = normalMap2.load()
    return [pixels,[normalImage.size[0],normalImage.size[1]],scale]

normalMap1 = Image.open(r"A:\files\code\github\pythonRayTracer\rendering python\normal maps\normalTest.png")
normalMap2 = Image.open(r"A:\files\code\github\pythonRayTracer\rendering python\normal maps\shapesNormal.jpg")
normalMap3 = Image.open(r"A:\files\code\github\pythonRayTracer\rendering python\normal maps\faceNormal.jpg")

ball1Pos = vector(1,0,4)
ball1Radius = 1
ball1Surface = surface(Color(100,100,200),matalicness=.0,opacity=0)

ball2Pos = vector(.5,2,4)
ball2Radius = 1
ball2Surface = surface(Color(200,100,100),matalicness=.0,opacity=0)

plane1Pos = vector(0,-1.25,0)
plane1Normal = vector(0,1,0)
plane1Surface = surface(color=Color(0,255,0),matalicness=.1,normalMap=getNormalInfo(normalMap2,scale=[1,1]))

ball1 = Prims.sphere(ball1Pos,ball1Radius,name="ball",surface= ball1Surface)
ball2 = Prims.sphere(ball2Pos,ball2Radius, surface=ball2Surface)
plane1 = Prims.plane(center=plane1Pos,normal=plane1Normal,surface=plane1Surface,name= "plane 1")
sun = Light.sunLight(vector(1,-1,0),1)

skySurface = surface((102,153,204))
skyColor = Color(102, 153, 204)


objects = [plane1,ball1,ball2]
lights = [sun]

def get():
    return objects,lights