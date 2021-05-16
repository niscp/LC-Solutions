class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        max_so_far = 0
        for item in height:
            if item > max_so_far:
                max_so_far = item
            left_max.append(max_so_far)
            
            
        right_max = []
        max_so_far_rt = 0
        for item_rt in height[::-1]:
            if item_rt > max_so_far_rt:
                max_so_far_rt = item_rt
            right_max.append(max_so_far_rt)
        right_max.reverse()
        water = 0
        for index in range(len(height)):
            water = water +  min(left_max[index], right_max[index]) - height[index]
        
        return water