class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def bfs(r,c,M):
            
            if (r,c,M) in memo:
                return memo[(r,c,M)]
            if r<0 or c<0 or r>=m or c>=n:
                return 1
            if M == 0:
                return 0
            ans = 0
            movements = [(1,0),(-1,0),(0,1),(0,-1)]
            for x,y in movements:
                ans += bfs(r+x, c+y, M-1)
            memo[(r,c,M)] = ans
            return ans
        return bfs(startRow, startColumn, maxMove)%(10**9+7)
        
        
        
        
        