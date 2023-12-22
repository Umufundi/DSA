from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        frequencies = Counter(word)

        for i in range(len(word)):
            remaining_word = word[:i] + word[i+1:]
            remaining_frequencies = Counter(remaining_word)
            
            if len(set(remaining_frequencies.values())) == 1:
                return True

        return False
