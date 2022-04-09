# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x  = str(x)
        x_len = len(str_x)

        if(x_len == 1):
            return True

        i = 0
        while i < int(x_len/2):
            if(str_x[i] != str_x[x_len-i-1]):
                return False
            i+=1


        return True

    def isPalindrome2(self, x: int) -> bool:

        str_x = str(x)
        rever_str_x = str_x[::-1]

        return str_x == rever_str_x

    def isPalindrome3(self, x: int) -> bool:

        str_x = str(x)
        rever_str_x = "".join(reversed(str_x))

        return str_x == rever_str_x
    

    def isPalindrome4(self, x: int) -> bool:
        
        if(x<0 or (x%10==0 and x!=0) ):
            return False

        reversed_num = 0
        while(reversed_num<x):
            reversed_num = reversed_num*10 + x%10
            x=int(x/10)
        print(x)
        print(reversed_num)
        return (reversed_num == x or int(reversed_num/10) == x)
        

def main():
    sol = Solution()
    res = sol.isPalindrome4(121)
    print(res)

    

if __name__ == "__main__":
    main()