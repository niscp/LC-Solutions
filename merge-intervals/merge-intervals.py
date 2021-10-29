class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x:x[0])
        if len(intervals) < 2:
            return intervals
        result = []
        interval_start = intervals[0][0]
        interval_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] > interval_end:
                # enw interval
                result.append([interval_start, interval_end])
                interval_start = interval[0]
                interval_end = interval[1]
            else:
                interval_start = min(interval_start, interval[0])
                interval_end = max(interval_end, interval[1])
        result.append([interval_start, interval_end])
        return result
