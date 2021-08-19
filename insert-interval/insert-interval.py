class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        start, end = 0, 1
        
        # discard all the intervals which ended before
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            result.append(intervals[i])
            i += 1
        
        # found the place merge wherever possible
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1
        
        result.append(newInterval)
        
        while i < len(intervals):
                result.append(intervals[i])
                i += 1
        
        return result