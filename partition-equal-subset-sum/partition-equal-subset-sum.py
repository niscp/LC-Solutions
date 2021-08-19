class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0:
            return False
        halfSum = sum(nums) /2 
        dp = {}
        return canPartition_recur(nums, 0, halfSum, dp)

def canPartition_recur(nums, current_index, target, dp):
    key = str(current_index) + ":" + str(target)
    if key in dp:
        return dp[key]
    if target == 0:
        return True
    if current_index >= len(nums):
        return False
    
    # include current element
    if nums[current_index] <= target:
        if canPartition_recur(nums, current_index+1, target - nums[current_index], dp):
            dp[key] = True
            return dp[key]        
    res = canPartition_recur(nums, current_index+1, target, dp)
    dp[key] = res
    return dp[key]