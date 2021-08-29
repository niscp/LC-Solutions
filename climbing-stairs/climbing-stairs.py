class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1 for _ in range(n+1)]
        return self.climbStairs_recur(n, dp)
    
    def climbStairs_recur(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        take1stepWay = self.climbStairs_recur(n-1, dp)
        take2stepWay = self.climbStairs_recur(n-2, dp)
        dp[n] = take1stepWay + take2stepWay
        return dp[n]