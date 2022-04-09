# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def conversion(self, s:str, numRows:int) -> str :

        if(numRows == 1):
            return s

        s_len = len(s)

        numCols = 0
        if(s_len <  2*numRows - 2):
            if(s_len<=numRows):
                numCols = 1
            else:
                numCols = 1 + s_len%numRows
        else:
            remainder = s_len%(2*numRows - 2)

            remain_cols = 0
            if (remainder == 0):
                remain_cols = 0
            elif (remainder <= numRows):
                remain_cols = 1
            else:
                remain_cols = 1 + remainder%numRows

            
            numCols = (1+numRows-2) * int(s_len/(2*numRows - 2)) + remain_cols

        ZagArray =  [['0' for i in range(numCols) ] for j in range(numRows) ]

        x, y = 0, 0
        for i, c in enumerate(s):
            iter = i % (2*numRows-2)
            ZagArray[y][x] = c
            if(iter < numRows-1):   
                y+=1   # go downward
            else:
                y-=1   # go upper-right
                x+=1
            #print(x,y)

        res = ''
        for i in range(numRows):
            for j in range(numCols):
                if ZagArray[i][j] != '0':
                    res += ZagArray[i][j]

        return res
        
class Solution2:
    def conversion(self, s:str, numRows:int) -> str :
        res = ''

        return res

def main():
    #sol = Solution()
    #test_s = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
    #res = sol.conversion(test_s, 10)
    c = "0"
    test = {}
    test[c] = 1
    print(test[c])
    #ZagArray = np.zeros([5,5])
    #test_array =  [[-1 for i in range(cols) ] for j in range(rows) ]
    #test_array = [['0']*cols]*rows
    #print(test_array)


if __name__ == "__main__":
    main()