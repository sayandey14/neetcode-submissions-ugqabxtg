class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        ans = []
        for i in range(len(strs)):
            dic = dict()
            for j in strs[i]:
                if j in dic:
                    dic[j] += 1
                else:
                    dic[j] = 0
            used = 0
            for k in range(len(arr)):
                if arr[k] == dic:
                    used = 1
                    ans[k].append(strs[i])
            if not used:
                arr.append(dic)
                ans.append([strs[i]])
        return ans
