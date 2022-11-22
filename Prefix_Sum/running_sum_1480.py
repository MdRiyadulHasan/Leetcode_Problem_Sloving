# prefix_sum
# palantir
class Solution:
    def runningSum(self, nums):
        self.sum =[]
        sum_till = 0
        for n in nums:
            sum_till+=n
            self.sum.append(sum_till)
        return self.sum
