class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        max_yet = 0
        for i in range(len(height)):
            left_max[i] = max_yet
            if height[i] > max_yet:
                max_yet = height[i]
        max_yet = 0
        for i in range(len(height)-1,-1,-1):
            right_max[i] = max_yet
            if height[i] > max_yet:
                max_yet = height[i]
                
        ans  = 0
        for i in range(1, len(height) - 1):
            water_here = min(left_max[i], right_max[i]) - height[i]
            if water_here > 0:
                ans += water_here
            
        return ans