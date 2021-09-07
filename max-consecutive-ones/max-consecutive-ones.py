class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        m = 0
        for item in nums:
            if item == 1:
                c += 1
            elif item == 0:
                c = 0
            m = max(m, c)
        return m