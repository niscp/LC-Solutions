import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        minRooms = 0
        minHeap = []
        
        for interval in intervals:
            #remove all that have ended
            while len(minHeap) > 0 and minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)
                
            heapq.heappush(minHeap, interval[1])
            
            minRooms = max(minRooms, len(minHeap))
            
        return minRooms
        
        