class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        path = []

        def dfs(open_, close_):
            if(open_ == close_ == n):
                temp = ""
                for i in path:
                    temp+=i
                ret.append(temp)
                return
            
            if(open_ < n):
                path.append("(")
                dfs(open_+1, close_)
                path.pop()
            
            if(close_ < open_):
                path.append(")")
                dfs(open_, close_+1)
                path.pop()
        
        dfs(0,0)

        return ret