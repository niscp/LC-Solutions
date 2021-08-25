class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        c = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != "1":
                    continue
                c += 1
                visitIsland(grid, row, col)
        return c
    
def visitIsland(grid, row, col):
    stack = [(row, col)]
    
    while len(stack):
        cr, cc = stack.pop()
        grid[cr][cc] = "0"
        nbrs = get_nbrs(grid, cr, cc)
        for nbr in nbrs:
            if grid[nbr[0]][nbr[1]] == "1":
                stack.append(nbr)

def get_nbrs(grid, row, col):
    rowLen = len(grid)
    colLen = len(grid[row])
    res = []    
    if row - 1 >=0:
        res.append((row-1, col))
    if col - 1 >=0:
        res.append((row, col-1))
    if row + 1 < rowLen:
        res.append((row+1, col))
    if col + 1 < colLen:
        res.append((row, col+1))
    return res