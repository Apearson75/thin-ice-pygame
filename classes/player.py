import pygame
from pygame.locals import *

from classes.level import Level

class Player:
    currentGridX = 1
    currentGridY = 1
    canMove = True
    dead = False
    deathTime = 0
    win = False
    winTick = 0

    def __init__(self, x, y, level: Level) -> None:
        self.gridX = x
        self.gridY = y
        self.level = level
        self.currentGridX = level.spawnCoordinates[0]
        self.currentGridY = level.spawnCoordinates[1]
        pass

    def draw(self, screen):
        x = (self.currentGridX * 600/self.gridX) + 15
        y = (self.currentGridY * 600/self.gridY) + 15
        pygame.draw.circle(screen, (255,0,0), (x, y), self.gridX/2)

    def checkState(self):
        currentTick = pygame.time.get_ticks()
        if self.dead and currentTick - self.deathTime >= 3000:
            print("Dead")
            pygame.quit()
        if self.win and currentTick - self.winTick >= 1000:
            print(f"You win, Score: {self.level.score}")
            pygame.quit()

    def playerMove(self, direction: str):
        if not self.dead and not self.win:
            if direction == "up" and self.currentGridY > 0:
                if self.level.getTile(self.currentGridX, self.currentGridY - 1)["type"] != "Wall":
                    self.currentGridY -= 1
                    self.level.setCurrentTile(self.currentGridX, self.currentGridY)
            elif direction == "down" and self.currentGridY < self.gridY - 1:
                if self.level.getTile(self.currentGridX, self.currentGridY + 1)["type"] != "Wall":
                    self.currentGridY += 1
                    self.level.setCurrentTile(self.currentGridX, self.currentGridY)
            elif direction == "left" and self.currentGridX > 0:
                if self.level.getTile(self.currentGridX - 1, self.currentGridY)["type"] != "Wall":
                    self.currentGridX -= 1
                    self.level.setCurrentTile(self.currentGridX, self.currentGridY)
            elif direction == "right" and self.currentGridX < self.gridX - 1:
                if self.level.getTile(self.currentGridX + 1, self.currentGridY)["type"] != "Wall":
                    self.currentGridX += 1
                    self.level.setCurrentTile(self.currentGridX, self.currentGridY)
        