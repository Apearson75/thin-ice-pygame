previousSpace = 0
lastTick = 0
cooldown = 150
currentSafePos = 0
forward = true

function platform()
    if currentSafePos == 19 and forward then
        forward = false
        setTileType(previousSpace, 12, "Safe")
        setTileType(currentSafePos, 12, "None")
        currentSafePos = 18
        previousSpace = 19
        return
    elseif currentSafePos == 0 and not forward then
        forward = true
        setTileType(previousSpace, 12, "Safe")
        setTileType(currentSafePos, 12, "None")
        currentSafePos = 1
        previousSpace = 0
        return
    end

    if forward then
        previousSpace = previousSpace + 1
        currentSafePos = previousSpace + 1
        setTileType(currentSafePos, 12, "Safe")
        setTileType(previousSpace, 12, "None")
    else
        previousSpace = previousSpace - 1
        currentSafePos = previousSpace - 1
        setTileType(currentSafePos, 12, "Safe")
        setTileType(previousSpace, 12, "None")
    end
end

function start()
    print("Moving platform mod ACTIVE")
end

function update(tick)
    if tick - lastTick > cooldown then
        lastTick = tick
        platform()
    end
end