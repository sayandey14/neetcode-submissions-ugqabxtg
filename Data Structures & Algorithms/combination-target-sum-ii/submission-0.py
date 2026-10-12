class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        path = []
        candidates.sort()
        def dfs(i, total):
            if(total == target):
                ret.append(path.copy())
                return
            if(i>= len(candidates)):
                return
            
            for choice in range(i, len(candidates)):
                if (choice > i and candidates[choice] == candidates[choice-1]):
                    continue
                
                if (total + candidates[choice] > target):
                    break
                
                path.append(candidates[choice])
                total += candidates[choice]
                dfs(choice + 1, total)
                total -= path.pop()
        
        dfs(0, 0)

        return ret
                    
