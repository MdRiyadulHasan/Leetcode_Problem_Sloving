# array
class Solution:
    def pivotIndex(self, nums) -> int:
        total = sum(nums)
        leftsum=0
        for i, val in enumerate(nums):
            rightsum=total-leftsum-val
            if leftsum==rightsum:
                return i
            leftsum=leftsum+val
        return -1
        