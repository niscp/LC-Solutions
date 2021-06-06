class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        right, ans = [0]*l,[0]*l,
        ans[0] = 1
        for index in range(1, l):
            ans[index] = ans[index-1]*nums[index-1]

        right[l-1] = 1
        for index in range(l-2, -1, -1):
            right[index] = right[index+1]*nums[index+1]

        for index in range(l):
            ans[index] = ans[index] * right[index]
        return ans
            
            
        