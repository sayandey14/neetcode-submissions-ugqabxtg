class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm = []
        rev = []
        for i in s:
            if i.isalnum():  
                norm.append(i.lower())
        for i in range(len(norm)-1,-1,-1):
            rev.append(norm[i])
        return(norm==rev)
