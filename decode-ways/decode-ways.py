class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        return numDecodings_recur(s, 0, dp)

def numDecodings_recur(s, current, dp):
    
    if current == len(s):
        return 1
    
    
    if s[current] == "0":
        return 0
    
    if current == len(s) - 1:
        return 1
    
    if current in dp:
        return dp[current]
    # either select single char or double if possible
    res = numDecodings_recur(s, current+1, dp)
    
    # double digit is only possible if it is less than 26.
    if int(s[current:current+2]) <= 26:
        res += numDecodings_recur(s, current+2, dp)
    dp[current] = res
    return dp[current] 
    
    
        