class Solution:
    def removeDuplicates(self,nums):
        l=1
        n=len(nums)
        for r in range(1,n):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l=l+1
        return l
if __name__ == '__main__':
    s=Solution()
    nums=list(map(int,input().strip().split()))
    result= s.removeDuplicates(nums)
    print(result)
