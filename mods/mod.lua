function start()
    print("Modded by lua")
end

function update(tick)
    local playerPos = getPosition()
    local x = playerPos[0]
    local y = playerPos[1]
    if tick > 3000 then -- After 3 seconds
        setTileType(8, 4, "Goal") -- Change tile (8,4) to a Goal Tile
        print("Set Goal at (8,4)")
    end
end