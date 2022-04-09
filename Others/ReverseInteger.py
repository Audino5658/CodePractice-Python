import math

class Solution:
    def ingerLength(self, x):
        res = 0
        while (x>=1):
            x = x / 10
            res += 1
        
        return res
        

    def reverse(self, x: int) -> int:
        MIN = - pow(2, 31)
        MAX = pow(2, 31) - 1

        res = 0
        if x <= MIN or x >= MAX:
            return res

        is_nagtive = False
        if  x < 0:
            is_nagtive = True
            x = -x

        cur_exp = self.ingerLength(x) -1
        new_exp = 0
        while( x > 0):
            res += int(x / pow(10, cur_exp)) * pow(10, new_exp)
            if res <= MIN or res >= MAX:  # Check whether new result bigger or smaller than than the range 
                return 0
            x=int(x % pow(10, cur_exp))   # next x

            cur_exp-=1
            new_exp+=1

        if is_nagtive:
            res = -res

        return res

class OfficialSolution:

    def reverse(self, x:int) -> int:

        INT_MAX = pow(2, 31)
        INT_MIN = - pow(2, 31)

        res = 0
        is_neg = False
        if x < 0:
            x = -x
            is_neg = True  

        while(x != 0):
            pop = x % 10
            if res > INT_MAX/10 or (res == INT_MAX / 10 and pop > 7): 
                return 0
            if res < INT_MIN/10 or (res == INT_MIN / 10 and pop < -8):
                return 0

            res = res*10 + pop
            x = int(x/10)

        if(is_neg):
            res = -res

        return res

def main():

    #sol = Solution() 
    #res = sol.reverse(1534236469)
    #print(res)

    sol2 = OfficialSolution()
    res = sol2.reverse(-1534)

    print(res)
    #print(-123%10)
    '''
    print(pow(2, 31) - 1)
    print(9646324351)
    #print(int(124%100))
    x = 9646324351
    if x > -2147483648 and x < 2147483647:
        print("enter") 
    '''
    

if __name__ == "__main__":
    main()
        