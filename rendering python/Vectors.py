import math
class vector:
    x = 0
    y = 0
    z = 0
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,vec):
        a = self.x + vec.x
        b = self.y + vec.y
        c = self.z + vec.z
        return vector(a,b,c)
    def __sub__(self,vec):
        a = self.x - vec.x
        b = self.y - vec.y
        c = self.z - vec.z
        return vector(a,b,c)
    def __mul__(self,vec):
        if type(vec) == int or type(vec) == float: 
            return vector(self.x*vec,self.y*vec,self.z*vec)
        return self.x * vec.x + self.y*vec.y + self.z*vec.z
    def __str__(self):
        return f"<{self.x},{self.y},{self.z}>"
    def mag(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def normalize(self):
        self.x /= math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        self.y /= math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        self.z /= math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def normal(self):
        a = self.x / math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        b = self.y / math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        c = self.z / math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        return vector(a,b,c)
    def rotateVector(self, vec2):
        xRot = vec2.x
        yRot = vec2.y
        zRot = vec2.z

        cosa = math.cos(zRot)
        sina = math.sin(zRot)

        cosb = math.cos(yRot)
        sinb = math.sin(yRot)

        cosc = math.cos(xRot)
        sinc = math.sin(xRot)

        Axx = cosa * cosb
        Axy = cosa * sinb * sinc - sina * cosc
        Axz = cosa * sinb * cosc + sina * sinc

        Ayx = sina * cosb
        Ayy = sina * sinb * sinc + cosa * cosc
        Ayz = sina * sinb * cosc - cosa * sinc

        Azx = -sinb
        Azy = cosb * sinc
        Azz = cosb * cosc

        px = self.x
        py = self.y
        pz = self.z

        pointx = Axx * px + Axy * py + Axz * pz
        pointy = Ayx * px + Ayy * py + Ayz * pz
        pointz = Azx * px + Azy * py + Azz * pz
        return vector(pointx, pointy, pointz)   
    def vecAngles(self):
        a = math.acos((self*vector(1,0,0))/self.mag())
        b = math.acos((self*vector(0,1,0))/self.mag())
        c = math.acos((self*vector(0,0,1))/self.mag())
        return vector(a,b,c)
    def neg(self):
        return self*(-1)