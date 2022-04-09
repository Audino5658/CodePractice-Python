#https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        
        max_value = 0
        res = 0
        for i, n in enumerate(nums) :
            if n > max_value:
                max_value = n 
                res = i
        
        for i, n in enumerate(nums) :
            if i != res and 2*n > max_value:
                res = -1

        return res

def main():

    nums = [1]

    sol = Solution()
    res = sol.dominantIndex(nums)
    print(res)

    

if __name__ == "__main__":
    main()