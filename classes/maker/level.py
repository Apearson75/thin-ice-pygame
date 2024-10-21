import pygame
import sys
from pygame.locals import *
import time
import json

class Level:
    cooldown = 450
    grid = []
    currentTile = None
    currentTileIndex = -1

    def __init__(self, x, y, level = None) -> None:
        try:
            with open(level, "r") as r:
                self.grid = json.load(r)
        except IndexError:
            print("Couldn't open")
            for i in range(x):
                for j in range(y):
                    square = {
                        "i": i,
                        "j": j,
                        "x": i * 600/x,
                        "y": j * 600/y,
                        "size": (600/x, 600/y),
                        "rectValue": (i * 600/x, j * 600/y, 600/x, 600/y),
                        "type": "Ice"
                    }
                    self.grid.append(square)

        
    def draw(self, screen):
        for square in self.grid:
            if square["type"] == "None":
                pygame.draw.rect(screen, (0,0,0), square["rectValue"])
            elif square["type"] == "Ice":
                pygame.draw.rect(screen, (0,0,0), square["rectValue"], 1)
            elif square["type"] == "Goal":
                pygame.draw.rect(screen, (255,255,0), square["rectValue"])
            elif square["type"] == "Wall":
                pygame.draw.rect(screen, (200,200,200), square["rectValue"])
            elif square["type"] == "Spawn":
                pygame.draw.rect(screen, (0,0,255), square["rectValue"])
            elif square["type"] == "Safe":
                pygame.draw.rect(screen, (0,255,0), square["rectValue"])
    
    def setPlayer(self, player):
        self.player = player

    def checkCurrentTile(self):
        if self.deathTiles != []:
            currentTick = pygame.time.get_ticks()
            for i,t in enumerate(self.deathTicks):
                if currentTick - t >= self.cooldown:
                    tile = self.grid[self.deathTilesIndexes[i]]
                    if self.player.currentGridY == tile["j"] and self.player.currentGridX == tile["i"]:
                        time.sleep(1)
                        pygame.quit()
                    tile["isGone"] = True
    
    def keyHandle(self, key):
        currentPos = (self.currentTile["i"], self.currentTile["j"])
        changedTile = self.grid[self.currentTileIndex]
        if key == K_w:
            print(f"Wall {currentPos}")
            changedTile["type"] = "Wall"
        elif key == K_g:
            print(f"Goal {currentPos}")
            changedTile["type"] = "Goal"
        elif key == K_s:
            print(f"Spawn {currentPos}")
            changedTile["type"] = "Spawn"
        elif key == K_i:
            print(f"Ice {currentPos}")
            changedTile["type"] = "Ice"
        elif key == K_n:
            print(f"None {currentPos}")
            changedTile["type"] = "None"
        elif key == K_o:
            print(f"Safe {currentPos}")
            changedTile["type"] = "Safe"
    
    def setCurrentTile(self, x, y):
        self.currentTile = [s for s in self.grid if s["i"] == x and s["j"] == y][0]
        self.currentTileIndex = [i for i,s in enumerate(self.grid) if s["i"] == x and s["j"] == y][0]

def drawStyleRect(surface, x, y):
    pygame.draw.rect(surface, (0,0,0), (x,y,150,150), 1)
