from heapq import *
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        f = {}
        for word in words:
            if word not in f:
                f[word] = 0
            f[word] += 1
            
        max_heap = []
        for w, v in f.items():
            heappush(max_heap, (-v, w))
        
        r = []
        for i in range(k):
            count, word = heappop(max_heap)
            r.append(word)
            
        return r
        