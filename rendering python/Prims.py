from tkinter.messagebox import RETRY
from Vectors import vector
from Surface import surface
import math
class base:
    surfaces = surface(255,255,255)
    pos = vector(0,0,0)
    name = ""
    def __init__(self,position,name = "no name",surface = surface(255,255,255)) -> None:
        self.surfaces = surface
        self.pos = position
        self.name = name
        pass
    def getByRay(self,startPos,startRay):
        return 0,vector(0,0,0),vector(0,0,0)
class sphere(base):
    surfaces = surface(255,255,255)
    pos = vector(0,0,0)
    radius = 1
    name = ""
    def __init__(self,position,radius,name = "no name",surface = surface(255,255,255)) -> None:
        self.surfaces = surface
        self.pos = position
        self.radius = radius
        self.name = name
        pass
    def getByRay(self, startPos, startRay):
        a = startRay*startRay
        b = startRay*2*(startPos-self.pos)
        c = (startPos-self.pos)*(startPos-self.pos) - self.radius*self.radius
        hits = b*b-4*a*c
        if(hits >= 0):
            distance = (startRay*(-2) * (startPos-self.pos) - math.sqrt(hits))/((startRay*startRay)*2)
            hitPoint:vector = startPos + startRay.normal()*distance
            normal = (hitPoint-self.pos).normal()
            return distance,hitPoint,normal
        return super().getByRay(startPos,startRay)
class plane(base):
    normal = vector(1,0,0)
    surfaces = surface()
    center = vector(0,0,0)
    name= ""
    def __init__(self,normal:vector,surface = surface(),center = vector(0,0,0),name = "no name" ) -> None:
        self.name = name
        self.center = center
        self.normal = normal
        self.surfaces = surface
        pass
    def getByRay(self, startPos, startRay):
        if startRay*self.normal != 0:
            dist = ((self.center-startPos)*self.normal)/(self.normal * startRay)
            hitpoint = startPos + (startRay*dist)
        if(dist > 0):
            return dist,hitpoint,self.normal
        return super().getByRay(startPos, startRay)