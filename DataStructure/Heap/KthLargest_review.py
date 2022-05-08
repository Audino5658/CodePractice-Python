#https://leetcode.com/problems/kth-largest-element-in-a-stream/

#Reference
#https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        
        self.heap_nums = nums
        heapq.heapify(self.heap_nums)
        self.k = k

        while len(self.heap_nums) > self.k:
            heapq.heappop(self.heap_nums)


    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap_nums, val)
        while( len(self.heap_nums) > self.k ):
            heapq.heappop(self.heap_nums)


        return self.heap_nums[0]





def main():

    k = 3
    nums = [4, 5, 8, 2]

    obj = KthLargest(k, nums)
    param_1 = obj.add(3)
    param_2 = obj.add(5)
    param_3 = obj.add(10)
    param_4 = obj.add(9)
    print(param_4)

    

if __name__ == "__main__":
    main()