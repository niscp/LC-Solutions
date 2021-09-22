from heapq import *
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fmap = {}
        for num in nums:
            if num not in fmap:
                fmap[num] = 0
            fmap[num] += 1
        min_heap = []
        for num, count in fmap.items():
            if len(min_heap) < k:
                heappush(min_heap, (count, num))
            else:
                min_count, m_num = min_heap[0]
                if count > min_count:
                    heappop(min_heap)
                    heappush(min_heap, (count, num))
        res = []
        for item in min_heap:
            res.append(item[1])
        
        return res
    
"""
fmap = {4 : 1, 1:1, -1 : 2, 2 : 2,3: 1 }
min_heap = [(2, 2), (2, -1)]
"""