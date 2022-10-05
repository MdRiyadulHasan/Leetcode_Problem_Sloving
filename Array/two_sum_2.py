class Solution:
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)-1
        while(l<r):
            current_sum=numbers[l]+numbers[r]
            if current_sum==target:
                return [l+1, r+1]
            elif current_sum<target:
                l=l+1
            else:
                r=r-1
if __name__ == '__main__':
    s=Solution()
    target=int(input())
    nums=list(map(int,input().strip().split()))
    result= s.twoSum(nums,target)
    print(result)
