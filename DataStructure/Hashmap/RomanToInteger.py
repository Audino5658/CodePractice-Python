class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
        convert_num = []
        for c in s:
            if( not c in symbols):
                continue
            else:
                convert_num.append(symbols[c])

        sum = 0
        for i in range(len(convert_num)):
            if i == len(convert_num) - 1 : # i = n-1
                sum += convert_num[i]
            else:
                if (convert_num[i] < convert_num[i+1]):  # i < n-1
                    sum -= convert_num[i]
                else:
                    sum += convert_num[i]
        return sum

def main():

    #sol = Solution() 
    #res = sol.reverse(1534236469)
    #print(res)

    sol = Solution()
    res = sol.romanToInt("LVIII")
    print(res)

    

if __name__ == "__main__":
    main()
        