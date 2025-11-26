# https://leetcode.com/problems/relative-ranks/description/

import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        answer = [0] * n
        box = [[v, i]for i, v in enumerate(score)]
        heapq.heapify(box)
        medal = {1:'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
        while box:
            _, i = heapq.heappop(box)
            answer[i] = medal[n] if n in medal else f"{n}"
            n -= 1
        return answer