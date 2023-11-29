class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ref_str = strs[0]
        common_prefix = []
        
        for i in range(len(ref_str)):
            if all(i<len(s) and s[i] == ref_str[i] for s in strs):
                common_prefix.append(ref_str[i])
            else:
                break
        return ''.join(common_prefix)
        