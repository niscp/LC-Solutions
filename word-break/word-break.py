class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = {}
        return wb_recur(s, frozenset(wordDict), 0, dp)


def wb_recur(s, word_dict, start, dp):
    if start in dp:
        return dp[start]

    if start == len(s):
        return True
    for end in range(start+1, len(s) + 1):
        if s[start:end] in word_dict and wb_recur(s, word_dict, end, dp):
            dp[start] = True
            return True
    dp[start] = False
    return False