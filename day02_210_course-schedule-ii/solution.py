# Day 02 - LeetCode 210: Course Schedule II
# Write your solution here.

from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, box = defaultdict(set), set(range(numCourses))
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[b].add(a)
            if a in box: box.remove(a)
            indegree[a] += 1

        answer = []
        stack = deque(box)
        while stack:
            node = stack.pop()
            answer.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1 
                if indegree[nxt] == 0:
                    box.add(nxt), stack.append(nxt)

        return answer if len(answer) == numCourses else []