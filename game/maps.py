"""Map generation for rogue."""

from __future__ import annotations

import attrs
import random
from enum import Enum

from typing import Final, Self, List

import utilities as u

class Map:
    """Generator for maps."""
    map_grid: List[int] = []
    room_list: List[Room] = []
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

    def _append_rooms(self, room_count: int, room_x_size: int, room_y_size: int) -> None:
        """Fit a list of room objects into map"""
        while len(self.room_list) < room_count:
            rand_x_pos: int = random.randrange(0, self.x_size, 1)
            rand_y_pos: int = random.randrange(0, self.y_size, 1)
            temp_room = Room(rand_x_pos, rand_y_pos, room_x_size, room_y_size)
            
            # Check if room will overlap with pre-existing walls or will be within 3 cells in x or y position
            if (self._is_room_available(temp_room)):
                for x in range(temp_room.x_size):
                    for y in range(temp_room.y_size):         
                        self.map_grid[temp_room.rect_x_pos + x][temp_room.rect_y_pos + y] = 2
                self.room_list.append(temp_room)

        # Create corridors (sort list of rooms)
        self.room_list.sort(key=lambda x: x.rect_x_pos, reverse=False)
        for x in range(len(self.room_list)-1):
            self._create_corridor(self.room_list[x], self.room_list[x+1])

    def _create_corridor(self, a: Room, b: Room):
        x1, y1, w1, h1 = a.rect_x_pos, a.rect_y_pos, a.x_size, a.y_size
        x2, y2, w2, h2 = b.rect_x_pos, b.rect_y_pos, b.x_size, b.y_size

        if (x1 + w1 < x2 or x2 + w2 < x1): # Vertical transition
            print(f"Writing vertical transition: x1: {x1}, w1: {w1}, x2: {x2}, w2: {w2}")
            x_rand: int
            a_rand_wall: int 
            b_rand_wall: int

            if (x1 + w1 < x2):
                x_rand = random.randrange(x1 + w1 + 1, x2 - 1, 1)
                a_rand_wall = random.randrange(y1 + 1, y1 + h1 - 1, 1)
                b_rand_wall = random.randrange(y2 + 1, y2 + h2 - 1, 1)
                print(f"A Random Wall: {x1}, {a_rand_wall}, B Random Wall: {x2}, {b_rand_wall}, Middle: {x_rand}")
            elif (x1 + w1 > x2):
                x_rand = random.randrange(x2 + w2 - 1, x1 + 1, 1)
                a_rand_wall = random.randrange(y2 + 1, y2 + h2 - 1, 1)
                b_rand_wall = random.randrange(y1 + 1, y1 + h1 - 1, 1)
                print(f"A Random Wall: {x1}, {a_rand_wall}, B Random Wall: {x2}, {b_rand_wall}, Middle: {x_rand}")
            else:
                return None

            for iter in range(x1+w1, x_rand):
                self.map_grid[iter][a_rand_wall] = 1
            for iter in range(x_rand, x2):
                self.map_grid[iter][b_rand_wall] = 1
            if (a_rand_wall < b_rand_wall):
                for iter in range(a_rand_wall, b_rand_wall+1):
                    self.map_grid[x_rand][iter] = 1
            else:
                for iter in range(b_rand_wall, a_rand_wall+1):
                    self.map_grid[x_rand][iter] = 1

        elif (y1 + h1 < y2 or y2 + h2 < y1): # Horizontal transition
            print(f"Writing horizontal transition: y1: {y1}, h1: {h1}, y2: {y2}, h2: {h2}")
            y_rand: int
            a_rand_wall: int
            b_rand_wall: int

            if (y1 + h1 < y2):
                y_rand = random.randrange(y1 + h1 + 1, y2 - 1, 1)
                a_rand_wall = random.randrange(x1 + 1, x1 + w1 - 1, 1)
                b_rand_wall = random.randrange(x2 + 1, x2 + w2 - 1, 1)
                print(f"A Random Wall: {x1}, {a_rand_wall}, B Random Wall: {x2}, {b_rand_wall}, Middle: {y_rand}")
            elif (y1 + h1 > y2):
                y_rand = random.randrange(y2 + h2 - 1, y1 + 1, 1)
                a_rand_wall = random.randrange(x2 + 1, x2 + w2 - 1, 1)
                b_rand_wall = random.randrange(x1 + 1, x1 + w1 - 1, 1)
                print(f"A Random Wall: {x1}, {a_rand_wall}, B Random Wall: {x2}, {b_rand_wall}, Middle: {y_rand}")
            else:
                return None

            if (y1+h1 > y2): # Determine whether room a is first or second from left
                for iter in range(y_rand, y1): # Do a rand wall to middle y position
                    self.map_grid[b_rand_wall][iter] = 1
                for iter in range(y2+h2, y_rand): # Do b rand wall to middle y position
                    self.map_grid[a_rand_wall][iter] = 1
            else:
                for iter in range(y1+h1, y_rand): # Do a rand wall to middle y position
                    self.map_grid[a_rand_wall][iter] = 1
                for iter in range(y_rand, y2): # Do b rand wall to middle y position
                    self.map_grid[b_rand_wall][iter] = 1
            if (a_rand_wall < b_rand_wall):
                for iter in range(a_rand_wall, b_rand_wall+1):
                    self.map_grid[iter][y_rand] = 1
            else:
                for iter in range(b_rand_wall, a_rand_wall+1):
                    self.map_grid[iter][y_rand] = 1

    def _is_room_available(self, room: Room) -> bool:
        """Check if other room already exists in current room boundary."""
        if (room.rect_x_pos + room.x_size + 1 < self.x_size and room.rect_y_pos + room.y_size + 1 < self.y_size): # Check if room size + position is within map
            if (room.rect_x_pos >= 0 and room.rect_y_pos >= 0): # Check if room is in negative bounds
                for x in range(room.x_size):
                    for y in range(room.y_size):
                        if (self.map_grid[room.rect_x_pos + x][room.rect_y_pos + y] == 2): # Check if room already exists in map position
                            if (self.map_grid[room.rect_x_pos + x - 3][room.rect_y_pos + y - 3] == 2 or self.map_grid[room.rect_x_pos + x + 3][room.rect_y_pos + y + 3] == 2): # Check if room exists -3 cells
                                return False
                            return False
            else:
                return False
        else:
            return False

        return True

    def _check_if_rooms_touch(self, a: Room, b: Room) -> bool:
        x1, y1, w1, h1 = a.rect_x_pos, a.rect_y_pos, a.x_size, a.y_size
        x2, y2, w2, h2 = b.rect_x_pos, b.rect_y_pos, b.x_size, b.y_size

        if (x1+w1 == x2 or x2+w2 == x1): # Touching x
            return True
        elif (y1+h1 == y2 or y2 + h2 == y1): # Touching y
            return True
        elif (x1+w1+3 >= x2 or x2+w2+3 >= x1): # 3 cell gap x
            return True
        elif (y1+h1+3 >= y2 or y2+h2+3 >= y1): # 3 cell gap y
            return True
        else:
            return False

    def get_map_grid(self) -> List[int]:
        return self.map_grid
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

temp_map = Map(500, 500)
temp_map._append_rooms(10, 50, 50)
u.create_image_from_map(temp_map.map_grid, "C:\\Users\\grant\\OneDrive\\Documents\\GitHub\\Gork\\data\\test.png")