class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                border = (row == 0 or row == len(grid) -1) or (col == 0 or col == len(grid[row]) -1)
                if not border:
                    continue
                if grid[row][col] != 1:
                    continue
                
                visit_all_nbrs(grid, row, col)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    count += 1
                if grid[row][col] == 2:
                    grid[row][col] = 1
                
                    
        return count

        
                
def visit_all_nbrs(grid, row, col):
    stack = [(row, col)]
    while len(stack):
        crow, ccol = stack.pop()
        grid[crow][ccol] = 2
        nbrs = get_nbrs(grid, crow, ccol)
        for nbr in nbrs:
            if grid[nbr[0]][nbr[1]] == 1:
                stack.append(nbr)

def get_nbrs(grid, row, col):
    res = []
    rowLen = len(grid)
    colLen = len(grid[row])
    
    if row - 1>= 0:
        res.append((row-1, col))
    if col - 1>= 0:
        res.append((row, col-1))
    if row + 1 < rowLen:
        res.append((row+1, col))
    if col + 1 < colLen:
        res.append((row, col+1))
    return res
        