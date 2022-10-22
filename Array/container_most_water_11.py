# array | two-pointers
# bloomberg
class Solution:
    def maxArea(self, height) -> int:
        l,r=0,len(height)-1
        res=0
        while l<r:
            area = (r-l)*min(height[l],height[r])
            res=max(res,area)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return res