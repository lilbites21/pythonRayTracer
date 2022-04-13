from pygame import Color
from Vectors import vector
import pygame
class surface:
    color = pygame.Color(255,255,255)
    matlicness = 0
    oppacity = 0
    normalMap = [vector(0,0,1),0,0]
    def __init__(self,color = Color(255,255,255),matalicness = 0,opacity = 0, normalMap = [vector(0,0,1),[1000,1000],[5,5]]) -> None:
        self.color = color
        self.matlicness = matalicness
        self.opacity = opacity
        self.normalMap = normalMap
        pass
