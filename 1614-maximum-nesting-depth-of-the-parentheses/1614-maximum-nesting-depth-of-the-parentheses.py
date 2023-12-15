class Solution:
    def maxDepth(self, s: str) -> int:
        
        open, deep = 0, 0
        for i in s:
            if i == "(": open +=1
            elif i == ")": open -=1
            deep = max(deep, open)
        return deep
        