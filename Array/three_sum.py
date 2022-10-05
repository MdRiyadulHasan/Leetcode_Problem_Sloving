class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets=[]
        length=len(nums)
        for i, a in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=length-1
            while l<r:
                current_sum=a+nums[l]+nums[r]
                if current_sum<0:
                    l=l+1
                elif current_sum>0:
                    r=r-1
                else:
                    triplets.append([a,nums[l],nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
        return triplets
if __name__ == '__main__':
    s=Solution()
    nums=list(map(int,input().strip().split()))
    result=s.threeSum(nums)
    print(result)
        