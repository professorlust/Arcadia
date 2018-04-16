-- player.lua

function Player(grill,x,y)
	local grill = grill
	local time = 0
	local player = {
		name = "player",
		x=x,
		y=y,
		size=grill.tile,
		speed = 0.1
	}
	function player.draw()
		love.graphics.setColor(0, 255, 0)
  		love.graphics.rectangle("fill", player.x*player.size, player.y*player.size, player.size, player.size)
	end

	function player.update(dt)
		time = time + dt
		if time > player.speed then
			player.move()
			time = 0
		end
	end

	function player.move()
		player.dx, player.dy = 0,0
		if love.keyboard.isDown("right") then
			player.dx = 1
		elseif love.keyboard.isDown("left") then
			player.dx = -1
		elseif love.keyboard.isDown("up") then
			player.dy = -1
		elseif love.keyboard.isDown("down") then
			player.dy = 1
		end
		if not player.group.collide(player) then
			player.x = player.x + player.dx
			player.y = player.y + player.dy
		end

		if player.x > grill.tile_w then
			player.x = 0
		end
	end

	return player
end

return Player
