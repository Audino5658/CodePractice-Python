#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict={}

        for n in nums:
            if n in dict:
                return True
            dict[n] = 1                

        return False

    def containsDuplicate2(self, nums: list[int]) -> bool:
        S = set()
        
        for x in nums:
            if x in S: 
                return True
            S.add(x)

def main():

    nums = [1,2,3,1]

    sol = Solution()
    res = sol.containsDuplicate(nums)
    print(res)

    

if __name__ == "__main__":
    main()