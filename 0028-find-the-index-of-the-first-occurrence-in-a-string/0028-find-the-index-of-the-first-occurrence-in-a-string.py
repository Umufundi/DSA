class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        i,j = 0, len(needle) 
        while j <= len(haystack): 
            if haystack[i:j] == needle:
                return i
            i += 1
            j += 1
        return -1