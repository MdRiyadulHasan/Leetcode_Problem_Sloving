# math | binary-search
# apple | bloomberg | facebook
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l=1
        r=x
        while(l<=r):
            mid=(l+r)//2
            mid_sq=mid*mid
            if mid_sq==x:
                return mid
            elif mid_sq>x:
                r=mid-1
            else:
                l=mid+1
                ans=mid
        return ans