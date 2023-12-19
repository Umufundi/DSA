class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        result = []
        for i in range(numRows):
            level = [1]*(i+1)
            for j in range(1, i):
                level[j] = result[i-1][j-1]+ result[i-1][j]
                
            result.append(level)
            
        return result
        
        
        