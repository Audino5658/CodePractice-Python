from collections import deque
from os import _exit

class Solution:

    def possibilityOfEscape(self, maze_mtx: list, h: int, w: int, start:list) -> bool:
       
        exit_pos = []
        for i in range(w):
            exit_pos.append([0, i])
            exit_pos.append([h-1, i])
        for i in range(1,h-1):
            exit_pos.append([i, 0])
            exit_pos.append([i, w-1])

        '''
        for i in range(h):
            for j in range(w):
                if  [i,j] in exit_pos:
                    print('.', end='')
                else:
                    print('#', end='')
            print()      
        '''
        queue = deque()
        visited = [[False]*w for x in range(h)]
        directions = [[0,1], [0,-1], [1,0], [-1, 0]]

        queue.appendleft(start)

        while len(queue) > 0:
            coord = queue.pop()
            #print(coord)
            if coord in exit_pos:
                return True

            visited[coord[0]][coord[1]] = True

            for dir in directions:
                ni, nj = [coord[0]+dir[0], coord[1] + dir[1]]
                #print(ni, nj)
                if (ni>=0 and ni<h and nj>=0 and nj<w and maze_mtx[ni][nj] != '#' and not visited[ni][nj]):
                    queue.appendleft([ni, nj])


        return False


def main():

    # Using readlines()
    file1 = open('DataStructure/Matrix/input.txt', 'r')
    first_line = file1.readline()
    size = first_line.split(' ',1)
    
    height, width = int(size[0]), int(size[1])
    #print(height)
    #print(width)

    # Initialize
    maze_array = [ ['#']*width for x in range(height)]
    start_coord = [0,0]
    startPoint = 0
    for i in range(height):
        input_line = file1.readline()
        if 'S' in input_line or '.' in input_line or '#' in input_line:
            for j in range(width):  
                if  j < len(input_line):          
                    maze_array[i][j] = input_line[j]  
                    #print(maze_array[i][j], end='')
                    if maze_array[i][j] == 'S':
                        start_coord = [i, j]
                        startPoint += 1
            #print()
            
    if startPoint != 1:
        print("NO")
        return 
 
    sol = Solution()
    res = sol.possibilityOfEscape(maze_array, height, width, start_coord)
    if res:
        print("YES")
    else:
        print("NO")
    

if __name__ == "__main__":
    main()