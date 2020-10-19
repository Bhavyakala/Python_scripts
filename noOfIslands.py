# QUESTION
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is
# surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
# may assume all four edges of the grid are all surrounded by water.

# Example input

# Input: grid = [ 
#     [ "1", "1", "1", "1", "0"], 
#     [ "1", "1", "0", "1", "0"], 
#     [ "1", "1", "0", "0", "0"], 
#     [ "0", "0", "0", "0", "0"]  
# ] 

# Output: 1 

import numpy as np

class Graph:
    nbr = [-1,0,1, 0] # utility arrays  
    nbc = [ 0,1,0,-1] # for exploring adjacent lands
    grid = [[]] #input grid
    ROWS = 0 # No. of rows
    COLS = 0 # No. of columns
    vis  = [[]] 
    
    def __init__(self,row, col, g):
        self.grid = g
        self.ROWS = row
        self.COLS = col
        self.vis = [[False for j in range(self.COLS)] for i in range(self.ROWS)]
    
    # Function to check for valid indexes of grid (i,j)
    def isSafe(self,i,j):
        if i>=0 and i<self.ROWS and j>=0 and j<self.COLS:
            return True
        else :
            return False
    # Functin of Depth first Search (dfs) for exploring the lands
    def dfs(self,i,j):
        self.vis[i][j] = True
        for x in range(4):
            cr = i + self.nbr[x]
            cc = j + self.nbc[x]
            if self.isSafe(cr,cc) and not self.vis[cr][cc] and self.grid[cr][cc]=='1':
                self.dfs(cr,cc)
    # Function to count no of islands by finding no of connected components in the grid
    def numIslands(self) :
        count = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if not self.vis[i][j] and self.grid[i][j]=='1':
                    count+=1
                    self.dfs(i,j)
        return count    
  
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
row = len(grid)
col = len(grid[0])
g = Graph(row,col,grid)
print(np.matrix(grid))
print(g.numIslands())