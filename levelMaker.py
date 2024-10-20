import pygame
import json
from pygame.locals import *
from classes.maker.level import Level
from classes.maker.player import Player

def reset():
    Player.currentGridX = 1
    Player.currentGridY = 1

    Level.grid = []
    Level.currentTile = None
    Level.currentTileIndex = -1

def editor(levelfile: str):
    pygame.init()

    slices = 20

    window_width = 600
    window_height = 600
    window_size = (window_width, window_height)

    window = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()

    level = Level(20, 20, levelfile)
    player = Player(20, 20, level)
    level.setPlayer(player)

    pygame.display.set_caption("Thin Ice Level Editor")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lastGrid = level.grid
                saveFile = ""
                if levelfile == None:
                    saveFile = "levels/level.json"
                else:
                    saveFile = levelfile
                with open(saveFile, "w") as w:
                    json.dump(lastGrid, w, indent=2)
                running = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == K_LEFT:
                    player.playerMove("left")
                elif key == K_RIGHT:
                    player.playerMove("right")
                elif key == K_UP:
                    player.playerMove("up")
                elif key == K_DOWN:
                    player.playerMove("down")
                else:
                    level.keyHandle(key)



        window.fill((255, 255, 255))
        # classes.level.drawStyleRect(window, 0, 0)


        level.draw(window)
        player.draw(window)


        pygame.display.flip()
        clock.tick(60)
    reset()
    pygame.quit()