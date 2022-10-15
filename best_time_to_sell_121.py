# array | dynamic-programming
# amazon | bloomberg | facebook | microsoft | uber
class Solution:
    def maxProfit(self, prices) -> int:
        l=0
        r=1
        maxprice=0
        while r<len(prices):
            if prices[l]<prices[r]:
                price=prices[r]-prices[l]
                maxprice=max(maxprice,price)
            else:
                l=r
            r=r+1
        return maxprice