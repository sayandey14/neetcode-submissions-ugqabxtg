class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []

        path = []
        
        def isP(string, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            return True
        
        def dfs(i):
            if i>= len(s):
                ret.append(path.copy())
                return
            
            for choice in range(i, len(s)):
                if isP(s, i, choice):
                    path.append(s[i:choice+1])
                    dfs(choice+1)
                    path.pop()
    
        
        dfs(0)
        return ret
        

