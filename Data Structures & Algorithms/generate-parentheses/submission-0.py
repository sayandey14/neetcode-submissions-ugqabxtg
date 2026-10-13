class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        path = []

        def dfs(open_, close):
            #base case:
            if(open_ == close and open_ + close == 2*n):
                ret.append("".join(path))
                return
            
            if open_ < n:
                path.append("(")
                dfs(open_+1, close)
                path.pop()

            if(close < open_):
                path.append(")")
                dfs(open_, close+1)
                path.pop()

        dfs(0,0)
        return ret    
            
        