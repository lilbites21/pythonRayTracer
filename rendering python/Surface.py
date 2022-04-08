from pygame import color
import pygame
class surface:
    color = pygame.Color(255,255,255)
    matlicness = 0;
    oppacity = 0;
    def __init__(self,color = pygame.Color(255,255,255),matalicness = 0,opacity = 0) -> None:
        self.color = color
        self.matlicness = matalicness
        self.opacity = opacity
        pass