# dynamic-programming
# 
class NumArray:

    def __init__(self, nums):
        self.sum = []
        sum_till =0
        for n in nums:
            sum_till+=n
            self.sum.append(sum_till)
    def sumRange(self, left: int, right: int) -> int:
        if left!=0:
            return self.sum[right]-self.sum[left-1]
        else:
            return self.sum[right]