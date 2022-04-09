## https://leetcode.com/problems/roman-to-integer/

class Solution:
    def roman_converter(self, cur_value, ten_count, l_c, m_c, r_c):
        # ex: C, L, X. exp = 1, current value = 85
        m_val = 5 * ten_count   #  L = 50 
        convert_roman = ""

        m_num = int( cur_value / m_val )        # 85 / 50 = 1
        cur_value = cur_value % m_val           # 85 % 50 = 35

        r_num = int(cur_value/ten_count )    #  r_num = 35 / 10 = 3

        if(m_num == 1):                             # Check whether L exists
            if(cur_value >= 4 * ten_count ):     # if current value >= 40  
                convert_roman += (r_c +l_c)         # XC
            else:
                convert_roman += m_c + r_c*r_num    # else L+(X*n)
        else:
            if(cur_value >= 4 * ten_count ):    # if current value >= 40
                convert_roman += (r_c + m_c)        # XL
            else:
                convert_roman += r_c * r_num        # X*n    (35 : XXX)
        
        next_value = cur_value % ten_count     # next value = 35 % 10 = 5

        return next_value, convert_roman

    def intToRoman(self, num: int) -> str:
        
        #rom_dict = {'M':0,'D':0, 'C':0,'L':0,'X':0 ,'V':0,'I':0}
        roman_str = "" 

        if len(str(num)) == 4:
            m_num = int( num / 1000 )
            roman_str += m_num * "M"
            num = num % 1000

        if  len(str(num)) == 3:
            num, convert_str = self.roman_converter( num, 100, 'M', 'D', 'C')
            roman_str += convert_str

        if  len(str(num)) == 2:
            num, convert_str = self.roman_converter( num, 10, 'C', 'L', 'X')
            roman_str += convert_str
            
        if  len(str(num)) == 1:
            num, convert_str = self.roman_converter( num, 1, 'X', 'V', 'I')
            roman_str += convert_str

        return roman_str

    def intToRoman2(self, num: int) -> str:

        #roman_str = 
        
        return 0

def main():
    sol = Solution()
    res = sol.intToRoman(1994)
    print(res)
    '''
    s = ""
    test = s + ('x'*3)
    print(test+'ss')
    '''

if __name__ == "__main__":
    main()