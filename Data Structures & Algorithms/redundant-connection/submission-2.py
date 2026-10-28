class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        degree = [0] * (n+1)
        graph = [[] for i in range(n+1)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
        
        queue = deque()

        for i in range(1,n+1):
            if degree[i] == 1:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            degree[node] -=1
            for neighbor in graph[node]:
                degree[neighbor] -=1
                if degree[neighbor] == 1:
                    queue.append(neighbor)
        
        for i in range(len(edges)-1,-1,-1):
            u,v = edges[i]
            if degree[u] >= 2 and degree[v] >= 2:
                return [u,v]
        return []


        
