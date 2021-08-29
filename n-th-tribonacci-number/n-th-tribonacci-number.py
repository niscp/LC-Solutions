class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1 for _ in range(n+1)]
        return self.tribonacci_recur(n, dp)

    def tribonacci_recur(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        
        if n == 0:
            return 0
        if n == 1 or n ==2:
            return 1
        dp[n] = self.tribonacci_recur(n-1, dp) + self.tribonacci_recur(n-2, dp) + self.tribonacci_recur(n-3, dp)
        return dp[n]
        
        