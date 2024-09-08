from PIL import Image
import numpy as np

from typing import List

def create_image_from_map(grid: List[List[int]], save_path: str, show: bool = False) -> None:
    temp_grid = []

    for row in grid:
        temp_row = []
        for value in row:
            if value == 1: 
                temp_row.append([255, 255, 255])
            elif value == 2:
                temp_row.append([255, 0, 0])
            elif value == 0:
                temp_row.append([0, 0, 0])
        
        temp_grid.append(temp_row)

    img = Image.fromarray(np.array(temp_grid, dtype=np.uint8), mode="RGB")
    img.save(save_path)

    if show:
        img.show()
