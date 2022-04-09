#https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        
        # push the new element and pop one element up to get the largest 3 elements  
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap) 

        return self.heap[0]
        




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