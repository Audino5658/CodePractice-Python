# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose 
        for i in range (n):
            for j in  range (n-i-1):
                row = i
                col = j+i+1
                tmp_val = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp_val
 
        # Reverse
        for i in range (n):
            for j in  range (int(n/2)):
                tmp_val = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = tmp_val

        print(matrix)
        return 
   

def main():
    matrix = [[1,2],[3,4]]
    sol = Solution()  
    sol.rotate([[1,2],[3,4]])
    


if __name__ == "__main__":
    main()