class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_so_far = nums[0]
        for item in nums[1:]:
            current_sum = max(item, current_sum + item)
            max_so_far = max(current_sum, max_so_far)


        return max_so_far
        
        