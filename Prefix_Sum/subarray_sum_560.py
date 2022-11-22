# array | hash-table
# google
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        sumdict = {0:1}
        s=0
        count = 0
        for n in nums:
            s+=n
            if s-k in sumdict:
                count+=sumdict[s-k]
            if s in sumdict:
                sumdict[s]+=1
            else:
                sumdict[s]=1
        return count
if __name__ == '__main__':
    nums = [3,4,7,2,-3,1,4,2,1]
    k = 7
    ob = Solution()
    ans = ob.subarraySum(nums, k)
    print(ans)