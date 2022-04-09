class Solution:
    def myAtoi(self, s:str) -> int :
        digit_array = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        signs =  {'-': 1,'+': 0}
        
        prev_digit = False
        is_nagtive = False
        is_float = False

        digit_count = 0
        sign_count = 0
        dot_pos = 0
        res_num = 0
        for c in s[::-1]:
            
            if(c in signs):
                is_nagtive = signs[c]
                sign_count+=1

            if (c == '.' and prev_digit):
                is_float = True
                dot_pos = digit_count

            if(c in digit_array):
                res_num += digit_array[c] * pow(10, digit_count)
                digit_count += 1
                prev_digit = True
            elif(c != '.'):  # if wword except '.' is found
                prev_digit = False


            if(not c in digit_array and not c in signs and digit_count>0 and c!=' ' and c!='.'): # basic rule of excluding illegal words
                return 0
                
            if(sign_count>1):  # multiple signs 
                return 0
            
            if(digit_count>0 and c in digit_array and not prev_digit): # words found among the integer 
                return 0

        if(is_float):
            res_num = int(res_num*pow(10, -dot_pos))

        if (is_nagtive):
            res_num = -res_num

        if(res_num > pow(2, 31) -1 ):
            res_num = pow(2, 31) -1
            
        if(res_num < -pow(2, 31) ):
            res_num = -pow(2, 31)

        return res_num
        

class Solution2:
    def myAtoi(self, s:str) -> int:

        digit_array = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        signs =  {'-': 1,'+': 0}

        res_num = 0
        digit_count = 0
        sign_count = 0
        float_pos = 0
        is_negative = False
        is_float = False
        for c in s:
            if (c == ' 'and digit_count == 0 and sign_count<1):  #"  +  413"
                continue
            elif(c in signs and digit_count == 0): # Include the case -12..., and 00000-42a1234
                sign_count += 1
                is_negative = signs[c]
                if(sign_count > 1 and digit_count == 0):  # the case +-12
                    return 0
            elif(c == '.' and digit_count > 0): # the case 3.11124...
                is_float = True
                float_pos = digit_count
            elif(not c in digit_array and digit_count == 0 ): #the case: aabbcc12223, -aa+12,
                return 0
            elif(c in digit_array):
                res_num = 10*res_num + digit_array[c]
                digit_count+=1
            elif(not c in digit_array and digit_count > 0): #the case: 12223aab ...
                break
            
        if is_float:
            res_num = int( res_num * pow(10, -(digit_count-float_pos) ) )
        if is_negative:
            res_num = -res_num
        
        if(res_num > pow(2, 31) -1 ):
            res_num = pow(2, 31) -1
            
        if(res_num < -pow(2, 31) ):
            res_num = -pow(2, 31)

        return res_num
    
    def myAtoi2(self, s:str) -> int:
        s = s.strip()
        num, i, sign, n = 0, 0, 1, len(s)
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            i+=1
        if s[0] == '+':
            i+=1
            
        while i < n:
            dg = ord(s[i]) - ord('0')
            if dg >= 0 and dg <= 9:
                num = (num*10) + dg
            else:
                break
            i+=1
        num = sign * num
        if num < -(2**31):
            return -(2**31)
        if num > (2**31) -1:
            return (2**31) -1
        return num


def main():
    s = "   -3.1456"
    sol2 = Solution2()
    #res = sol2.myAtoi(s)

    res2 = sol2.myAtoi2(s)
    print(res2)
    
    #for c in s[::-1]:
    #    print(c)

if __name__ == "__main__":
    main()