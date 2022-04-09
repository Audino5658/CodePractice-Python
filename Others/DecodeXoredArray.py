class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        decode_list = []
        decode_list.append(first)

        prev_e = first
        for e in encoded:
            decoded_e = prev_e^e
            decode_list.append(prev_e^e) 
            prev_e = decoded_e
        
        return decode_list
            
   

def main():
    encoded = [1,2,3]
    first = 1
    sol = Solution()  
    ans = sol.decode(encoded,first)

    print(1^2)
    # 3 = 2 XOR 1     A = B XOR C
    # 1 = 2 XOR 3     C = B XOR A
    


if __name__ == "__main__":
    main()