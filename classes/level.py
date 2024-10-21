import pygame
import time
import json

class Level:
    cooldown = 450
    score = 0
    grid = []
    deathTicks = []
    deathTiles = []
    deathTilesIndexes = []
    currentTile = None
    spawnCoordinates = (1, 1)

    def __init__(self, x, y, level) -> None:
        with open(level, "r") as r:
            self.grid = json.load(r)
            for tile in self.grid:
                if tile["type"] == "Spawn":
                    self.spawnCoordinates = (tile["i"], tile["j"])
                    self.currentTile = tile
    
        
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
    
    def setPlayer(self, player):
        self.player = player

    def checkCurrentTile(self):
        if self.deathTiles != []:
            currentTick = pygame.time.get_ticks()
            for i,t in enumerate(self.deathTicks):
                tile = self.grid[self.deathTilesIndexes[i]]
                if currentTick - t >= self.cooldown and tile["type"] != "None":
                    if self.player.currentGridY == tile["j"] and self.player.currentGridX == tile["i"]:
                        self.player.dead = True
                        self.player.deadTime = pygame.time.get_ticks()
                    tile["type"] = "None"
        if self.currentTile["type"] == "Goal" and not self.player.win:
            self.player.win = True
            self.player.winTick = pygame.time.get_ticks()
    
    # I am not proud of what i've done - Shahid
    def setCurrentTile(self, x, y):
        s = [s for s in self.grid if s["i"] == x and s["j"] == y][0]
        if s["type"] == "None":
            self.player.dead = True
            self.player.deadTime = pygame.time.get_ticks()
        elif s["type"] == "Ice":
            self.deathTicks.append(pygame.time.get_ticks())
            self.deathTiles.append([s for s in self.grid if s["i"] == x and s["j"] == y][0])
            self.deathTilesIndexes.append([i for i,s in enumerate(self.grid) if s["i"] == x and s["j"] == y][0])
            self.score += 1
            print(f"Score: {self.score}")
        self.currentTile = s

    def getTile(self, x, y):
        return [s for s in self.grid if s["i"] == x and s["j"] == y][0]
    
    def getTileIndex(self, x, y):
        return [i for i,s in enumerate(self.grid) if s["i"] == x and s["j"] == y][0]
    
    def setTileType(self, x, y, type):
        i = self.getTileIndex(x, y)
        self.grid[i]["type"] = type


def drawStyleRect(surface, x, y):
    pygame.draw.rect(surface, (0,0,0), (x,y,150,150), 1)
