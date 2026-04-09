class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        ans = []
        for i in range(len(strs)):
            dic = {}
            for j in strs[i]:
                dic[j] = 1 + dic.get(j, 0)
            used = 0
            for k in range(len(arr)):
                if arr[k] == dic:
                    used = 1
                    ans[k].append(strs[i])
            if not used:
                arr.append(dic)
                ans.append([strs[i]])
        return ans
        #arr holds the first instance of every unique dict we see
