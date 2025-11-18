# https://leetcode.com/problems/kth-largest-element-in-a-stream/?utm_source=chatgpt.com

import heapq
INF = 10**8

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-INF]
        while nums:
            if len(self.nums) >= k:
                heapq.heappushpop(self.nums, nums.pop())
            else:
                heapq.heappush(self.nums, nums.pop())

    def add(self, val: int) -> int:
        heapq.heappushpop(self.nums, val)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)