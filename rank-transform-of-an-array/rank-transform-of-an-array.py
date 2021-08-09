class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(set(arr))
        dict_a = {}
        arr_result = []

        for i,j in enumerate(sorted_arr,start=1):
          dict_a[j] = i

        for i in arr:
          arr_result.append(dict_a[i])
        
        return arr_result
