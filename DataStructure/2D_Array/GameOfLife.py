# https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        '''
        step1 :
        1, 0 : original board status
        2 : status from 0 to 1
        -1 : status from 1 to 0

        '''
        direct = [[-1,-1], [-1,0], [-1,1],  [0,-1], [0,1],  [1,-1], [1,0], [1,1]]
        for i in range (len(board)):
            for j in range (len(board[i])):
                liveCount = 0
                for d in direct:
                    neigh = [ i + d[0], j + d[1] ]
                    if (not neigh[0] < 0) and (not neigh[1] < 0) and (neigh[0] < len(board)) and (neigh[1] < len(board[i])):
                        if ( board[neigh[0]][neigh[1]] == 1 or board[neigh[0]][neigh[1]] == -1):
                            liveCount += 1
                    
                if board[i][j] == 1 and liveCount < 2 :
                    board[i][j] = -1
                elif board[i][j] == 1 and liveCount > 3 :
                    board[i][j] = -1
                elif board[i][j] == 0 and liveCount == 3 :
                    board[i][j] = 2

        '''
        step2 :
        Refresh the new status -1, 2 to 0, 1 in the board.
        '''
        for i in range (len(board)):
            for j in range (len(board[i])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

                #print(board[i][j], end=' ')
            
            #print("\n")


def main():

    input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sol = Solution()
    sol.gameOfLife(input)


if __name__ == "__main__":
    main()
