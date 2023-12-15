class Solution:
    def sortSentence(self, s: str) -> str:
        dictionary ={}
        list_words = s.split()
        for i in list_words:
            dictionary[i[-1]] = i[:-1]
        return ' '.join(dictionary[j] for j in sorted(dictionary))