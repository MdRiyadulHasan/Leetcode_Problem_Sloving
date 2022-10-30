# array | greedy
class Solution:
    def jump(self, nums):
        jump=0
        current=0
        farthest=0
        for i in range(len(nums)-1):
            farthest=max(farthest, i+nums[i])
            if (i==current):
                current=farthest
                jump+=1
        return jump