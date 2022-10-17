class Solution:
    def maxSubArray(self, nums) -> int:
        maxsub_ar=nums[0]
        cur_sum=0
        for num in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=num
            maxsub_ar=max(maxsub_ar,cur_sum)
        return maxsub_ar