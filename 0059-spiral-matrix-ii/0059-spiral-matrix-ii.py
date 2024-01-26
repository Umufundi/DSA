class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        '''
        
        right, left, top, bottom = n, 0, 0, n
        grid = [ [0 for j in n] for i in n ]
        last = 1
        while bottom == top or right == left
                if row >= right and col == top:
                    top -=1  
                if row >= right and col >= bottom:
                    right -=1
                if row == left and col >= bottom:
                    bottom +=1
                if row == left and col == top:
                    left +=1
                grid[i][j] += last
                last = grid[i][j]
        return grid
        
        
        
        '''
        # Initialize boundaries
        right, left, top, bottom = n - 1, 0, 0, n - 1
        grid = [[0 for _ in range(n)] for _ in range(n)]  # Use range(n) instead of n
        
        last = 1
        
        while left <= right and top <= bottom:  # Change the condition to a valid one
            # Move from left to right
            for col in range(left, right + 1):
                grid[top][col] = last
                last += 1
            top += 1
            
            # Move from top to bottom
            for row in range(top, bottom + 1):
                grid[row][right] = last
                last += 1
            right -= 1
            
            # Move from right to left
            if top <= bottom:  # Check if there are more rows to traverse
                for col in range(right, left - 1, -1):
                    grid[bottom][col] = last
                    last += 1
                bottom -= 1
            
            # Move from bottom to top
            if left <= right:  # Check if there are more columns to traverse
                for row in range(bottom, top - 1, -1):
                    grid[row][left] = last
                    last += 1
                left += 1
        
        return grid