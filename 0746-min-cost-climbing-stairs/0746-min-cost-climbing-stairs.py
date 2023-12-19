'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        
        if cost[0] + cost[2] > cost[1]: 
            result = cost[1]
        else:
            result = cost[0]
        for i in cost:
            #preferably make two steps
            if cost[i+1] > cost[i+2]:
                result+=cost[i+2]
            #unless it is better to make 1 step
            else:
                result+=cost[i+1]
        return result
        
 '''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        if n == 2:
            return min(cost)
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])

        
        