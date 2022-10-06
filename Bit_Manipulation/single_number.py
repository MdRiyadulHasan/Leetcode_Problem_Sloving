# hash-table | bit-manipulation
# airbnb | palantir
class Solution:
    def singleNumber(self, nums):
        res=0
        for n in nums:
            res=res^n
        return res
if __name__ == '__main__':
    s=Solution()
    nums=list(map(int,input().strip().split()))
    result= s.singleNumber(nums)
    print(result)