"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #copy
        hashmap = {None: None}

        def dfs(cur):
            if not cur:
                return
            if cur in hashmap:
                return hashmap[cur]
            
            copy = Node(cur.val)
            hashmap[cur] = copy

            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        

        return dfs(node)

        