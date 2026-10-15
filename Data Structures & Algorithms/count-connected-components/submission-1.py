class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        
        for u, v in edges:
            hashmap[u].append(v)
            hashmap[v].append(u)

        seen = set()
        components = 0

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbour in hashmap[node]:
                if neighbour not in seen:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in seen:
                components += 1
                dfs(i)
        
        return components

