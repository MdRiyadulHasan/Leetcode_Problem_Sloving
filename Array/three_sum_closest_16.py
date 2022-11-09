# array | two-pointers
# bloomberg 
def threeSumClosest( nums, target: int):
    nums.sort()
    res=sum(nums[:3])
    for i in range(len(nums)-2):
        l=i+1
        r=len(nums)-1
        while l<r:
            temp_sum=nums[i]+nums[l]+nums[r]
            if abs(temp_sum-target)<abs(res-target):
                res=temp_sum
            if temp_sum<target:
                l+=1
            else:
                r-=1
    return res
if __name__ == '__main__':
    target = 1
    nums = [1,2,-1,4]
    ans =threeSumClosest(nums,target)
    print(ans)
   