#array | binary-search

class Solution:
    def searchInsert(self, nums, target):
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            if target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return l
if __name__ == '__main__':
    ob=Solution()
    nums=list(map(int, input().strip().split()))
    target=int(input())
    ans=ob.searchInsert(nums,target)
    print(ans)