class Solution:
    def MaxSumOfSubarray(self, arr:list, k:int) -> int :

        n = len(arr)
        max_sum =  sum(arr[:k])
        cur_sum = max_sum

        for i in range(n-k):
            cur_sum = cur_sum - arr[i] + arr[i+k]
            max_sum = max(cur_sum, max_sum)

        return max_sum
        


def main():
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]

    sol = Solution()
    res = sol.MaxSumOfSubarray(arr, 4)
    print(res)



if __name__ == "__main__":
    main()