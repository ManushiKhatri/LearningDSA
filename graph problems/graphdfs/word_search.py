'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

'''
def word_search(board, word) -> bool:
    #edge case 
    if not board:
        return True 
    # check bounds 
    def inbounds(grid,row,col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])
    #dfs 
    def dfs(row,col,index):
        # base case 
        if len(word)==index:
            return True 
        if not inbounds(board,row,col) or word[index]!=board[row][col] or board[row][col]=='#':
            return False
        #marking visited 
        temp=board[row][col]
        board[row][col]='#'
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_r = row + dr
            new_c = col + dc
            if dfs(new_r,new_c,index+1):
                return True 
        #backtrack 
        board[row][col]=temp
        return False 
    #initiate starting point 
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==word[0] and dfs(row,col,0):
                return True
    return False 
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(word_search(board,word))