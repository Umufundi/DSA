class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = []
        for i, j in zip(word1, word2):
            result.append(i)
            result.append(j)
            
        result.extend(word1[len(word2):])
        result.extend(word2[len(word1):])
        
        return "".join(result)
                
        