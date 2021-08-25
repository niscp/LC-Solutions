class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[row])):
                rowIsBorder = row == 0 or row == len(board) - 1
                colIsBorder = col == 0 or col == len(board[row]) - 1
                if not (rowIsBorder or colIsBorder):
                    continue
                
                if board[row][col] != "O":
                    continue 
                
                visitAllNeighbors(board, row, col)
                
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "O":
                    board[row][col] = "X" 
                if board[row][col] == "m":
                    board[row][col] = "O" 
                
                
                
                
def visitAllNeighbors(board, row, col):
    stack = [(row, col)]
    
    while len(stack):
        currRow, currCol = stack.pop()
        if board[currRow][currCol] == "m":
            continue
            
        board[currRow][currCol] = "m"
        
        
        nbrs = get_nbrs_list(board, currRow, currCol)
        
        for nbr in nbrs:
            if board[nbr[0]][nbr[1]] != "O":
                continue
            stack.append(nbr)
        
            
def get_nbrs_list(board, row, col):
    rowLen = len(board)
    colLen = len(board[row])
    res = []
    #up
    if row - 1 >=0:
        res.append((row-1, col))

    #down
    if row + 1 < rowLen:
        res.append((row+1, col))

    #right
    if col + 1 < colLen:
        res.append((row, col+1))

    #left
    if col - 1 >= 0:
        res.append((row, col-1))
    
    return res
