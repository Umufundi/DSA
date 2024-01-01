class TrieNode:
    def __init__(self, val="#"):
        self.isEnd = False
        self.children = dict()
        self.val = val

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode(c)
                cur = cur.children[c]
            cur.isEnd = True
        res = len(s)
        dp = [len(s) for _ in range(len(s) + 1)]
        dp[0] = 0
        for start in range(len(s)):
            pre = root
            for end in range(start, len(s)):
                if s[end] not in pre.children:
                    dp[end + 1] = min(dp[end + 1], dp[end] + 1)
                    break
                else:
                    pre = pre.children[s[end]]
                    if pre.isEnd:
                        #print(f"pre = {pre.val} start = {s[start]} end = {s[end]}")
                        dp[end + 1] = min(dp[end + 1], dp[start])
                    else:
                        dp[end + 1] = min(dp[end + 1], dp[end] + 1)

        #print(dp)
        return dp[-1]