# array
# amazon | apple | facebook | linkedin | microsoft
class Solution:
    def productExceptSelf(self, nums):
        res = []
        product = 1
        for i in range(len(nums)):
            product*=nums[i]
            res.append(product)
        product = 1
        for i in range(len(nums)-1,0,-1):
            res [i] = res[i-1]*product
            product = product*nums[i]
        res[0] = product
        return res
if __name__ == '__main__':
    nums = [1,2,3,4]
    ob = Solution()
    ans = ob.productExceptSelf(nums)
    print(ans)