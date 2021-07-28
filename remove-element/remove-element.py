class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fp = 0
        sp = len(nums) - 1
        c = 0
        while fp <= sp:
            if nums[fp] == val:
                nums[fp] = nums[sp]
                c += 1
                sp -= 1
            else:
                fp += 1
        return len(nums) - c
        