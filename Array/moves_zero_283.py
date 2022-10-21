# array | two-pointers
# bloomberg | facebook
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while r<len(nums):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
            r=r+1