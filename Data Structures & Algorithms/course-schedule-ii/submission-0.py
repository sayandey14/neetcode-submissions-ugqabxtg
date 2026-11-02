class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i:[] for i in range(numCourses)}
        degree = [0]*(numCourses)

        for u,v in prerequisites:
            graph[v].append(u)
            degree[u]+=1
        
        queue = deque()
        path = []
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            path.append(cur)
            for neighbour in graph[cur]:
                degree[neighbour] -=1
                if degree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(path) == numCourses:
            return path
        else:
            return []
        
