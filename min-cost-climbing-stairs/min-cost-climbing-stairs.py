class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost = [0 for _ in range(len(cost) + 1)]
        for idx in range(2, len(cost)+1):
            take1step = min_cost[idx -1] + cost[idx-1]
            take2step = min_cost[idx -2] + cost[idx-2]
            min_cost[idx] = min(take1step, take2step)
        return min_cost[-1]
