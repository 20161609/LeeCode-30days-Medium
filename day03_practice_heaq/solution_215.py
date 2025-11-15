# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?utm_source=chatgpt.com

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        h = []
        for n in nums:
            heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]
    