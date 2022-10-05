# array | two-pointers
class Solution:
    def removeElement(self, nums,val):
        k=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=val:
                nums[k]=nums[i]
                k=k+1
        return k

if __name__ == '__main__':
    s=Solution()
    val=int(input())
    nums=list(map(int,input().strip().split()))
    result= s.removeElement(nums,val)
    print(result)
