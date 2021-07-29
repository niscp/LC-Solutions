class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        start = 0
        end = x - 1
        while start <= end:
            mid = (start + end)//2
            sq_here = mid*mid
            if sq_here == x:
                return mid
            elif sq_here < x:
                start = mid + 1
            else:
                end = mid - 1
        return end
            
            
        