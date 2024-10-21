import pygame
from pygame.locals import *
from lupa.lua54 import LuaRuntime
from classes.level import Level
from classes.player import Player

def reset():
    Player.currentGridX = 1
    Player.currentGridY = 1
    Player.canMove = True
    Player.dead = False
    Player.deathTime = 0
    Player.win = False
    Player.winTick = 0

    Level.score = 0
    Level.grid = []
    Level.deathTicks = []
    Level.deathTiles = []
    Level.deathTilesIndexes = []
    Level.currentTile = None
    Level.spawnCoordinates = (1, 1)

def main(levelfile: str):
    lua = LuaRuntime(unpack_returned_tuples=True)
    with open('mods/mod.lua', "r") as r:
        lua.execute(r.read())

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

    pygame.display.set_caption("Thin Ice")

    lua.globals().getTile = level.getTile
    lua.globals().setTileType = level.setTileType
    lua.globals().playerMove = player.playerMove
    lua.globals().getPosition = player.getPosition

    with open('mods/mod.lua', 'r') as r:
        lua.execute(r.read())
    
    if lua.globals().start != None:
        lua.globals().start()

    running = True
    finalStatus = "Unfinished"
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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



        window.fill((255, 255, 255))
        # classes.level.drawStyleRect(window, 0, 0)

        currentTick = pygame.time.get_ticks()
        if player.dead and currentTick - player.deathTime >= 3000:
            print("Dead")
            running = False
            finalStatus = "Dead"
        if player.win and currentTick - player.winTick >= 1000:
            print(f"You win, Score: {player.level.score}")
            running = False
            finalStatus = "Win"
        
        if lua.globals().update != None:
            lua.globals().update(currentTick)

        level.draw(window)
        level.checkCurrentTile()
        player.draw(window)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    reset()
    return [level.score, finalStatus]