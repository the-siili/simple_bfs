
import time
import os
from random import randint


def main():
    s = 9
    start_pos = (0, 0)
    end_pos = (6, 8)
    obs = 10


    while True:

        start_pos = (int(input("Start position X(0-8): ")), int(input("Start position Y(0-8): ")))
        end_pos = (int(input("End position X(0-8): ")), int(input("End position Y(0-8): ")))
        obs = int(input("Amount of obstacles: "))


        grid = generate_grid(s,start_pos,end_pos,obs)
        #print(grid)

        find_path(start_pos[0], start_pos[1], end_pos[0], end_pos[1], grid)

        if input("New Grid(y/n): ") == "n":
            break



class Tile:
    def __init__(self, x, y, path : list) -> None:
        self.pos = [y, x]
        self.path = path

    def __str__(self) -> str:
        return str(self.pos)








def find_path(current_x, current_y, end_x, end_y, map1:list):

    map = map1.copy()

    end = [end_y, end_x]

    start_tile =  Tile(current_x, current_y, [current_x, current_y])

    queue = [start_tile]
    found_tiles = []

    final_path = []

    for tile in queue:
        if tile.pos not in found_tiles:
            found_tiles.append(tile.pos)

        if tile.pos == end:
            final_path = tile.path
            break

        for t in find_neighbors(tile, map):
            new_path = tile.path.copy()
            new_path.append([t[1], t[0]])
            new_t = Tile(t[1], t[0], new_path)
            if t not in found_tiles:
                queue.append(new_t)

    
    for part in final_path:
        os.system('cls||clear')
        try:
            map[part[1]][part[0]] = "X"
        except:
            pass
        for line in map:
            for i in line:
                print(i, end=" ")
            print("")
        time.sleep(0.5)
        


        



def find_neighbors(tile, grid):
    top = (tile.pos[0]-1, tile.pos[1])
    bottom = (tile.pos[0]+1, tile.pos[1])
    left = (tile.pos[0], tile.pos[1]-1)
    right = (tile.pos[0], tile.pos[1]+1)


    result_tiles = []

    if -1 < top[0] < len(grid) and -1 < top[1] < len(grid) and grid[top[0]][top[1]] != 0:
        result_tiles.append([top[0], top[1]])

    if -1 < bottom[0] < len(grid) and -1 < bottom[1] < len(grid)  and grid[bottom[0]][bottom[1]] != 0:
        result_tiles.append([bottom[0], bottom[1]])

    if -1 < left[0] < len(grid[0]) and -1 < left[1] < len(grid[0])  and grid[left[0]][left[1]] != 0:
        result_tiles.append([left[0], left[1]])

    if -1 < right[0] < len(grid[0]) and -1 < right[1] < len(grid[0])  and grid[right[0]][right[1]] != 0:
        result_tiles.append([right[0], right[1]])

    if result_tiles != []:
        return result_tiles
    else: 
        return []


    

def generate_grid(size, start, end, obstacles):

    grid1 = []

    #creating blank grid
    for i in range(size):
        line = []
        for i in range(size):
            line.append(1)
        grid1.append(line)


    i = 0
    while i < obstacles:
        x = randint(0, size-1)
        y = randint(0, size-1)

        if grid1[y][x] != 0:
            grid1[y][x] = 0
            i+= 1

    #adding start and end point
    grid1[start[1]][start[0]] = "S"
    grid1[end[1]][end[0]] = "E"




    return grid1




main()