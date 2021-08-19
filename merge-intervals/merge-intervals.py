class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x:x[0])
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            # overlapping situation
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                result.append([start, end])
                start = interval[0]
                end = interval[1]
        result.append([start, end])
            
        
        return result
        