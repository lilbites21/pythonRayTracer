from Vectors import vector
from Surface import surface
import math



class base:
    surfaces = surface(255,255,255)
    pos = vector(0,0,0)
    name = ""
    normalMap = 0
    def __init__(self,position,name = "no name",surface = surface(255,255,255)) -> None:
        self.surfaces = surface
        self.pos = position
        self.name = name
        pass
    def getByRay(self,startPos,startRay):
        return 0,vector(0,0,0),vector(0,0,0)
    def getNormal(hitpoint:vector):
        return 0
class sphere(base):
    surfaces = surface(255,255,255)
    pos = vector(0,0,0)
    radius = 1
    name = ""
    normalMap = 0
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
            return distance,hitPoint,self.getNormal(hitPoint)
        return super().getByRay(startPos,startRay)
    
    def getNormal(self,hitpoint:vector):
        normal = (hitpoint-self.pos).normal()
        normalMap = self.surfaces.normalMap
        if(type(normalMap) == vector):
            return normal
        return normal
        
            
        
        

    
        
class plane(base):
    normal = vector(1,0,0)
    surfaces = surface()
    center = vector(0,0,0)
    name= ""
    normalMap = vector(0,0,1)
    def __init__(self,normal:vector,surface = surface(),center = vector(0,0,0),name = "no name",normalMap = vector(0,0,1)) -> None:
        self.name = name
        self.center = center
        self.normal = normal
        self.surfaces = surface
        self.normalMap = normalMap
        pass
    def getByRay(self, startPos:vector, startRay:vector):
        if startRay*self.normal != 0:
            dist = ((self.center-startPos)*self.normal)/(self.normal * startRay)
            hitpoint = startPos + (startRay*dist)
            if(dist > 0):
                return dist,hitpoint,self.getNormal(hitpoint)
        return super().getByRay(startPos, startRay)
    def getNormal(self,hitpoint: vector):
        normal = self.normal    
        normalMap,normalDim,normalScale = self.surfaces.normalMap[0], self.surfaces.normalMap[1], self.surfaces.normalMap[2]
        if(type(normalMap) == vector):
            return self.normal
        foo = type(normalMap)
        normalMap:foo = normalMap
        
        normalColor = normalMap[int((hitpoint.x/normalScale[0]%1)*normalDim[0]*.99),int((hitpoint.z/normalScale[1]%1)*normalDim[1]*.99)]
        normalizedNormalMapNormal = vector(normalColor[0]/255,normalColor[1]/255,normalColor[2]/255).normal()
        angles2 = normalizedNormalMapNormal.vecAngles()
        normal = normal.rotateVector(angles2)
        return normal
    def __str__(self):
        return f"name: {self.name};  normal:  {self.normal} ;  center:  {self.center}"
        