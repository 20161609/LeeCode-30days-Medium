# Note

## Code
``` python
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, box, indegree = defaultdict(set), set(range(numCourses)), defaultdict(int)
        for a, b in prerequisites:
            graph[b].add(a)
            if a in box: box.remove(a)
            indegree[a] += 1

        stack, answer = deque(box), []
        while stack:
            node = stack.pop()
            answer.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1 
                if indegree[nxt] == 0:
                    box.add(nxt), stack.append(nxt)

        return answer if len(answer) == numCourses else []
```

## Link
https://leetcode.com/problems/course-schedule-ii/

## Idea
- Topological Sort: Remember the number of edges connected with each node.
- How to code:
    - Create Graph with list `prerequisites`.
        - Using `Defaultdict(int)`, it can direct which node can be approched.
        - You should count each edges and store them.
    - BFS search:
        - Each node should be appended to `answer`.
        - Visiting each node, you should all edges connected with current node.
        - If a node doesn't have 0 edges, the node cannot be next node.
    - Return `answer`. But if its number is not matching `numCourses`, empty list(`[]`) should be returned.


## Complexity
- Time: O(n^2)
- Space: O(n^2)

## Review
- It's first time to use `Topological Sort`. It was ver interesting to remember the number of edges.