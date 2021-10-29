class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_max = [0 for _ in range(len(prices))]
        max_yet = 0
        for i in range(len(prices)-1, -1, -1):
            right_max[i] = max_yet
            if prices[i] > max_yet:
                max_yet = prices[i]
        result = 0
        for i in range(len(prices)):
            diff_here = right_max[i] - prices[i]
            if diff_here > result:
                result = diff_here
        
        return result
            
        