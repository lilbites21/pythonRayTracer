from Vectors import vector
class light:
    intencity = 10
    def getDir(self,position:vector):
        return 0
class sunLight(light):
    dir = vector(0,0,0)
    intencity = 1.0
    def __init__(self,direction:vector,intencity = 1) -> None:
        self.dir = direction.normal()
        self.intencity = intencity
        pass
    def getDir(self, p):
        return self.dir