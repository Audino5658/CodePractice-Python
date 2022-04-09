#https://leetcode.com/problems/next-greater-element-i/submissions/

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        dstTable ={}

        for i, dstNum in enumerate(nums2):
            dstTable[dstNum] = i

        nums2_len = len(nums2)
        for srcNum in nums1:
            srcNumPos = dstTable[srcNum]
            for i in range(srcNumPos, nums2_len):
                if nums2[i] > srcNum:
                    res.append(nums2[i])
                    break
                elif i ==  nums2_len-1:
                    res.append(-1)


        return res


def main():

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

    sol = Solution()
    res = sol.nextGreaterElement(nums1, nums2)
    print(res)


if __name__ == "__main__":
    main()