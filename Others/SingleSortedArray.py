class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        begin , end = 0, len(nums)-1

        while(end>begin+1): 
            mid = (int)((begin + end)/2)
            if(nums[mid]==nums[mid-1]):
                if (mid-1)%2==1:     # [1,1,2, 3,3, 4,4,8,8]
                    end = mid-2 
                else:                # [1,1,2,2 3,3, 4,4,5,8,8]
                    begin = mid+1
            elif(nums[mid]==nums[mid+1]):   
                if (mid)%2==1:    # [1,1,2, 4,4, 8,8]
                    end = mid-1    
                else:               # [1,1,3,3, 4,4, 5, 8,8]
                    begin = mid+2
            else:                   # [4,4,5,8,8]
                return nums[mid]

        # last 3 numbers will left at last   
        mid = (int)((begin + end)/2)
        if(nums[begin] == nums[mid]):
            return nums[end]
        else:
            return nums[begin]


def main():

    #arr = [3,3,7,7,10,11,11]
    #arr = [1,1,2,3,3,4,4,8,8]
    arr = [1,1,2,2, 3,3, 4,4,5,8,8]
    sol = Solution()
    res = sol.singleNonDuplicate(arr)
    print(res)

    

if __name__ == "__main__":
    main()