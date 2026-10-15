class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #is a tree if no cycles present in any edges
        # number of vertices = number of edges + 1
        #check if 

        #edge count property
        if len(edges) != n-1:
            return False

        #create tree
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        
        for u, v in edges:
            hashmap[u].append(v)
            hashmap[v].append(u)
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbour in hashmap[node]:
                if neighbour not in seen:
                    dfs(neighbour)
        
        dfs(0)

        return len(seen) == n