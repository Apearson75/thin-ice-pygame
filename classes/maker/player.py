import pygame
from pygame.locals import *

from classes.level import Level

class Player:
    currentGridX = 1
    currentGridY = 1
    canMove = True

    def __init__(self, x, y, level: Level) -> None:
        self.gridX = x
        self.gridY = y
        self.level = level
        pass

    def draw(self, screen):
        x = (self.currentGridX * 600/self.gridX) + 15
        y = (self.currentGridY * 600/self.gridY) + 15
        pygame.draw.circle(screen, (255,0,255), (x, y), self.gridX/2)

    def playerMove(self, direction: str):
        if direction == "up" and self.currentGridY > 0:
            self.currentGridY -= 1
            self.level.setCurrentTile(self.currentGridX, self.currentGridY)
        elif direction == "down" and self.currentGridY < self.gridY - 1:
            self.currentGridY += 1
            self.level.setCurrentTile(self.currentGridX, self.currentGridY)
        elif direction == "left" and self.currentGridX > 0:
            self.currentGridX -= 1
            self.level.setCurrentTile(self.currentGridX, self.currentGridY)
        elif direction == "right" and self.currentGridX < self.gridX - 1:
            self.currentGridX += 1
            self.level.setCurrentTile(self.currentGridX, self.currentGridY)
        