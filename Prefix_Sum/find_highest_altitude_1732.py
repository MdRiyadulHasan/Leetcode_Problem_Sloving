class Solution:
    def largestAltitude(self, gain) -> int:
        max_value = 0
        sum_till = 0
        for n in gain:
            sum_till+=n
            max_value = max(max_value,sum_till)
        return max_value