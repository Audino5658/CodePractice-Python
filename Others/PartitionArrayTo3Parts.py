class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        
        total = sum(arr)

        # Firstly, it should be able to be divided by 3 
        if (total%3 != 0):
            return False
        
        part_sum = total /3 

        part_i= 0
        part_count= 0
        for i,num in enumerate(arr):
            part_count += num
            if part_count == part_sum and part_i < 3:
                part_i += 1
                part_count= 0
            
            if(part_i==3 and i==len(arr)-1):
                return True


        return False
        



def main():
    #arr= [0,0,0,0]
    arr = [3,3,6,5,-2,2,5,1,-9,4]
    sol = Solution()
    ans = sol.canThreePartsEqualSum(arr)

    print(ans)


if __name__ == "__main__":
    main()