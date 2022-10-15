# linked-list | two-pointers
# amazon | facebook
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        l,r=0, len(nums)-1
        while l<r:
            if nums[l]!=nums[r]:
                return False
            l,r=l+1,r-1
        return True
        