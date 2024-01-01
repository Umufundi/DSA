class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        zeros_in_first = 0
        ones_in_second = s.count('1')

        # Iterate through the string, excluding the last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_in_first += 1
            else:
                ones_in_second -= 1

            current_score = zeros_in_first + ones_in_second
            max_score = max(max_score, current_score)

        return max_score
        