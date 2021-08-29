class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1 for _ in range(n+1)]
        return self.fib_recur(n, dp)
    
    def fib_recur(self, n, dp):
        if not dp[n] == -1:
           return dp[n] 
            
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp[n] = self.fib_recur(n-1, dp) + self.fib_recur(n-2, dp)
        return dp[n]
        
        
