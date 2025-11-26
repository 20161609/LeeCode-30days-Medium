# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

INF = 10**10
import heapq
from collections import deque

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        h = [(nums1[0] + nums2[0], 0, 0)]
        answer, v = [], set([0])
        while len(answer) < k:
            _sum, i, j = heapq.heappop(h)
            answer.append([nums1[i],nums2[j]])
            for ni, nj in [(i+1,j), (i, j+1)]:
                if not (ni<n1 and nj<n2) or (ni*n2+nj in v):
                    continue
                v.add(ni*n2+nj), heapq.heappush(h, (nums1[ni]+nums2[nj],ni,nj))
        return answer