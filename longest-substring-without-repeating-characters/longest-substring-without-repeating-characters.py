class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        result = 0
        char_map = {}
        for end in range(len(s)):
            right_char = s[end]
            if right_char in char_map:
                start = max(start, char_map[right_char] + 1)
            
            char_map[right_char] = end
            result = max(result, end - start + 1)

        return result 
    
        