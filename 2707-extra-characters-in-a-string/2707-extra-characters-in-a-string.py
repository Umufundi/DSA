class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = {}
        for word in dictionary:
            current = trie
            for char in word:
                current = current.setdefault(char, {})
            current[""] = None

        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n)[::-1]:
            dp[i] = dp[i + 1] + 1
            current = trie
            for j in range(i, n):
                if s[j] not in current:
                    break
                current = current[s[j]]
                if "" in current:
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]