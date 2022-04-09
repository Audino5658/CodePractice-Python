class Solution:
    def check(self, nums: list[int]) -> bool:
        length = len(nums)
        is_sorted = True

        # Check whether is sorted
        for i in range(1, length):
            if (nums[i-1] > nums[i]):
                is_sorted = False
                break

        if is_sorted:
            return True

        # Check whether can be rotated
        if nums[-1] > nums[0]:
            return False

        turningpoint = False
        for i in range(0, length):
            if i != 0:
                if not turningpoint:
                    if nums[i-1] > nums[i]:
                        turningpoint = True
                else:
                    if nums[i-1] > nums[i]:
                        return False
                

        return True

   

def main():
    nums = [1,3,2]
    sol = Solution()  
    res = sol.check(nums)
    print(res)

if __name__ == "__main__":
    main()