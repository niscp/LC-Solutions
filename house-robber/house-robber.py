class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1 for _ in range(len(nums))]
        return rob_recur(nums, 0, dp)
def rob_recur( nums, c, dp):
    if c >= len(nums):
        return 0
    if dp[c] != -1:
        return dp[c]
    cost1 = nums[c] + rob_recur(nums, c+2, dp)
    cost2 =  rob_recur(nums, c+1, dp)
    dp[c] = max(cost1, cost2)
    return dp[c]
        