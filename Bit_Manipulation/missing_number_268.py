class Solution:
    def missingNumber(self, nums):
        result=0
        for i, value in enumerate(nums):
            result=result^i+1
            result=result^value
        return result
if __name__ == '__main__':
    nums=list(map(int,input().strip().split()))
    s=Solution()
    ans=s.missingNumber(nums)
    print(ans)

    