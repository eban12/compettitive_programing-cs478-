class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i,j = click
        
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        elif board[i][j] == 'E':
            stack = []
            stack.append((i,j))
            while stack:
                x,y = stack.pop()
                temp = self.bfs(x,y,board)
                for k in temp:
                    stack.append(k)
        return board
        
    
    def bfs(self,i,j,board):
        queue = []
        mines = 0
        for x,y in [(i+1,j),(i-1,j),(i,j-1),(i-1,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1),(i,j+1)]:
            if 0<=x<len(board) and 0<=y<len(board[0]):
                if board[x][y] == 'E':
                    queue.append((x,y))
                elif board[x][y] == 'M':
                    mines += 1

        if mines != 0:
            board[i][j] = str(mines)
            return []
        else:
            board[i][j] = 'B'
            return queue
