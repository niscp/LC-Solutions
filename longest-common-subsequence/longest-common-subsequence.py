class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = {}
        return longestCommonSubsequence_recur(text1, text2, 0, 0, dp)
    
def longestCommonSubsequence_recur(text1, text2, index1, index2, dp):
    if index1 == len(text1) or index2 == len(text2):
        return 0
    key = str(index1) + "-" + str(index2)
    if key in dp:
        return dp[key]
    if text1[index1] == text2[index2]:
        return 1 + longestCommonSubsequence_recur(text1, text2, index1+1, index2+1, dp)
    c1 = longestCommonSubsequence_recur(text1, text2, index1+1, index2, dp)
    c2 = longestCommonSubsequence_recur(text1, text2, index1, index2+1, dp)
    dp[key] = max(c1, c2)
    return dp[key]