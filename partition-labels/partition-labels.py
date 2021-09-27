"""
s = aba bcb aca def egd ehijhk lij
last_occ_map = {}
window_start = 0
max_index = 8
result = []
window_end = 8
last_occ_here = 8
max_index = 8
window_start = 
"""

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occ_map = {}
        
        c = 0
        while c < len(s):
            last_occ_map[s[c]] = c
            c += 1
        
        window_start = 0
        max_index = last_occ_map[s[window_start]]
        result = []
        for window_end in range(len(s)):
            last_occ_here = last_occ_map[s[window_end]]
            max_index = max(max_index, last_occ_here)
            
            if window_end == max_index:
                result.append(window_end - window_start +1 )
                window_start = window_end +1
                if window_start < len(s):
                    max_index = last_occ_map[s[window_start]]
            
        return result