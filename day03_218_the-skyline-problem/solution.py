# Day 03 - LeetCode 218: The Skyline Problem
# Write your solution here.
from collections import defaultdict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # # 1️⃣ buildings 리스트에서 모든 "이벤트"를 추출한다.
        # #    - 건물이 시작할 때: (left, -height)
        # #    - 건물이 끝날 때: (right, height)
        # #    => 음수는 "시작", 양수는 "끝"을 뜻함
        events = []
        for l,r,h in buildings:
            events.append(l,-h), events.append(r,h)
        # for each building in buildings:
        #     left, right, height = building
        #     add (left, -height)   # 시작 이벤트
        #     add (right, height)   # 끝 이벤트

        # # 2️⃣ 이벤트를 x좌표 기준으로 정렬
        # #    - 같은 x에서는 시작(-height)이 끝(+height)보다 먼저 와야 함
        # #    - 시작 이벤트 중에서는 키 큰(-값 더 작음) 게 먼저 와야 함
        # sort events properly
        events.sort()

        # # 3️⃣ 우선순위 큐(heap) 준비
        # #    - 현재 “활성화된 건물들의 높이”를 담음
        # #    - 파이썬에선 heapq로 “최대힙” 대신 음수값을 넣는 방식 사용
        heap = [0]  # 지면 높이 0
        previous_max_height = 0
        result = []

        # # 4️⃣ 모든 이벤트를 순회하며 처리
        for x, h in events:
            if h < 0:
                heap.append(-h)
            else:
                
        # for x, h in events:
        #     if h < 0:
        #         # 시작 이벤트 → 건물 높이 추가
        #         push(-h) into heap
        #     else:
        #         # 끝 이벤트 → 건물 높이 제거
        #         remove h from heap   # (직접 제거 대신 lazy removal 고려 가능)

        #     # 현재 최고 높이(힙의 top 값)를 확인
        #     current_max = heap의 최대값

        #     # 높이가 바뀌었다면 skyline이 변한 것
        #     if current_max != previous_max_height:
        #         add [x, current_max] to result
        #         previous_max_height = current_max

        # # 5️⃣ 최종 result 반환
        # return result
