"""Map generation for rogue."""

from __future__ import annotations

import attrs
import random

from typing import Final, Self, List

class Map:
    """Generator for maps."""
    map_grid: List[int] = []
    x_size: int
    y_size: int

    def __init__(self, x_size: int, y_size: int):
        self.x_size = x_size
        self.y_size = y_size

        for x in range(x_size):
            self.map_grid.append([])
            for y in range(y_size):
                temp: int = 0
                self.map_grid[x].append(temp)

    def append_rooms(self, room_count: int) -> None:
        """Fit a list of room objects into map"""
        # Temp
        room_x_size = 5
        room_y_size = 5
        
        for x in range(room_count):            
            rand_x_pos: int = random.randrange(0, self.x_size, 1)
            rand_y_pos: int = random.randrange(0, self.y_size, 1)
            
            temp_room = Room(rand_x_pos, rand_y_pos, room_x_size, room_y_size)

            # Check if room will overlap with pre-existing walls
            if (self._is_room_available(temp_room)):
                for x in range(temp_room.x_size):
                    for y in range(temp_room.y_size):
                        self.map_grid[temp_room.rect_x_pos + x][temp_room.rect_y_pos + y] = 1

    def _is_room_available(self, room: Room) -> bool:
        """Check if other room already exists in current room boundary."""
        for x in range(room.x_size):
            for y in range(room.y_size):
                    print(f"Checking: {x}, {y}")
                    if (self.map_grid[room.rect_x_pos + x][room.rect_y_pos + y] == 1):
                        return False
                    else:
                        continue

    def get_map_grid(self) -> List[int]:
        return self.map_grid
    
    def __str__(self):
        print(self.map_grid)
    
class Room:
    """General room class for square/rectangular rooms"""
    x_size: int
    y_size: int
    rect_x_pos: int # left most
    rect_y_pos: int # top most
    wall_glyph: int = 1

    def __init__(self, rect_x_pos, rect_y_pos, x_size, y_size):
        self.rect_y_pos = rect_y_pos
        self.rect_x_pos = rect_x_pos
        self.x_size = x_size
        self.y_size = y_size

temp_map = Map(100, 100)
temp_map.append_rooms(5)
print(temp_map.map_grid)