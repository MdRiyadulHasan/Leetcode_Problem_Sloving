# stack
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        dict={}
        for n in nums2:
            while stack and stack[-1]<n:
                k=stack.pop()
                dict[k]=n
            stack.append(n)
        return [dict.get(i,-1) for i in nums1]