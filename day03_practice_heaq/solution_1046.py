# https://leetcode.com/problems/last-stone-weight/?utm_source=chatgpt.com

import heapq
from heapq import heappush, heapify, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] *= -1
            
        heapify(stones)
        while len(stones)>1:
            heappush(stones, heappop(stones)-heappop(stones))

        return -stones.pop()
    
# Runtime
# 0
# ms
# Beats
# 100.00%
# Analyze Complexity
# Memory
# 17.86
# MB
# Beats
# 31.14%