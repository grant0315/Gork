"""Map generation for rogue."""

from __future__ import annotations

import attrs
import random
from enum import Enum

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

    def _append_rooms(self, room_count: int) -> None:
        """Fit a list of room objects into map"""
        # Temp
        time_out: int = 50 # used to determine stop inifite retrys for room placement
        room_x_size = 5
        room_y_size = 5
        
        for x in range(room_count):
            time_out -= 1
            rand_x_pos: int = random.randrange(0, self.x_size, 1)
            rand_y_pos: int = random.randrange(0, self.y_size, 1)
            
            temp_room = Room(rand_x_pos, rand_y_pos, room_x_size, room_y_size)

            # Check if room will overlap with pre-existing walls
            if (self._is_room_available(temp_room) and time_out > 0):
                for x in range(temp_room.x_size):
                    for y in range(temp_room.y_size):
                        self.map_grid[temp_room.rect_x_pos + x][temp_room.rect_y_pos + y] = 1

    def _create_cooridor(self, a: Room, b: Room):
        x1, y1, w1, h1 = a.rect_x_pos, a.rect_y_pos, a.x_size, a.y_size
        x2, y2, w2, h2 = b.rect_x_pos, b.rect_y_pos, b.x_size, b.y_size

        if (x1 + w1 < x2 or x2 + w2 < x1): # Horizontal transition
            a_rand_wall = random.randrange(0, x1 + w1, 1)
            b_rand_wall = random.randrange(0, x2 + w2, 1)
            x_rand = random.randrange(x1 + w1, x2 + w2, 1)

            # Create line from rand wall a to x_rand
            for x in range(x1 - x_rand):
                self.map_grid[x1 + x][y1] == 1

        elif (y1 + h1 < y2 or y2 + h2 < y1): # Vertical transition
            a_rand_wall = random.randrange(0, y1 + h1, 1)
            b_rand_wall = random.randrange(0, y2 + h2, 1)
            y_rand = random.randrange(y1 + h1, y2 + h2, 1)

            # Create line from rand wall a to x_rand
            for y in range(y1 - y_rand):
                self.map_grid[y1 + y][x1] == 1

        """ elif ((x1 + w1 < x2 or x2 + w2 < x2) and (y1 + h1 < y2 or y2 + h2 < y1)): # Then random"""
        """ else: # They overlap and doesn't need to be connected via cooridor
            pass """
        

    def _is_room_available(self, room: Room) -> bool:
        """Check if other room already exists in current room boundary."""
        print(f"Room X: {room.rect_x_pos} -> {room.rect_x_pos + room.x_size}, {room.rect_y_pos} -> {room.rect_y_pos + room.y_size}")
        if (room.rect_x_pos + room.x_size < self.x_size and room.rect_y_pos + room.y_size < self.y_size): # Check if room size + position is within map
            for x in range(room.x_size):
                for y in range(room.y_size):
                    print(f"Checking: {room.rect_x_pos + x}, {room.rect_y_pos + y}")
                    if (self.map_grid[room.rect_x_pos + x][room.rect_y_pos + y] == 1): # Check if room already exists in map position
                        return False
                    else:
                        continue
        else:
            return False

        return True

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

class RoomType(Enum):
    """Enum containing different UID's for room types."""
    BASIC = 1
    CORRIDOR = 2
    TREASURE = 3
    TRAP = 4
    PUZZLE = 5
    LAIR = 6
    SHOP = 7
    SECRET = 8
    ENV_HAZARD = 9
    BOSS = 10
    PORTAL = 11
    ALTAR = 12
    ARCHIVE = 13

temp_map = Map(20, 20)
temp_map._append_rooms(10)
temp_map._create_cooridor()
for x in range(len(temp_map.map_grid)):
    print(temp_map.map_grid[x])