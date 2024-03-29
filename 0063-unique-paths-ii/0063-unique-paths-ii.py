class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        """
        m = len(grid)
        n = len(grid[0])
        
        #path count
        if r == m-1 and c == n-1:
            return 1
        #change direction
        #obstacle
        if obstacleGrid[r][c] == 1
        #right top
        if obstacleGrid[r][c] 
        #left bottom
        if obstacleGrid[r][c]
        
        ans += dfs()
        
        
        """
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Helper function for recursive DFS
        def dfs(r, c):
            # Check if out of bounds or obstacle
            if r < 0 or c < 0 or r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            
            # Check if reached the destination
            if r == m - 1 and c == n - 1:
                return 1
            
            # If already visited, return the stored result
            if (r, c) in memo:
                return memo[(r, c)]
            
            # Recursive DFS to explore right and down directions
            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            
            # Update and store the result in the memoization dictionary
            memo[(r, c)] = right + down
            
            return memo[(r, c)]
        
        # Initialize memoization dictionary
        memo = {}
        
        # Start DFS from the top-left corner
        return dfs(0, 0)