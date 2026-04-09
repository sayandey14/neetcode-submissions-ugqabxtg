from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
            slen = len(s)
            tlen = len(t)

            if slen != tlen:
                return False
            
            slist = []
            for i in s:
                slist.append(i)
            slist.sort()
            
            tlist = []
            for i in t:
                tlist.append(i)
            tlist.sort()

            for i in range(slen):
                if slist[i] != tlist[i]:
                    return False
            return True
        
        final_list = []
        length = len(strs)
        seen = [False] * length  # Track processed strings with a boolean array

        for i in range(length):
            if seen[i]:  # Skip already processed strings
                continue
            temp = [strs[i]]
            seen[i] = True  # Mark the current string as seen
            for j in range(i + 1, length):
                if not seen[j] and isAnagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    seen[j] = True  # Mark as seen
            final_list.append(temp)

        final_list.sort(key=lambda cur: len(cur))
        return final_list
