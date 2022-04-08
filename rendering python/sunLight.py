from Vectors import vector
class sunLight:

    dir = vector(0,0,0)
    intencity = 1.0;
    def __init__(self,direction:vector,intencity = 1) -> None:
        self.dir = direction.normal()
        self.intencity = intencity
        pass