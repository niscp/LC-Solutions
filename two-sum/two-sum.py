# hash map approach : O(n) with space O(n)
# 2 pointers : O(nlogn) with O(1) space

# approach 1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(nums)):
            r = target - nums[i]
            if r in h:
                return [h.get(r), i]
            else:
                h[nums[i]] = i
        
