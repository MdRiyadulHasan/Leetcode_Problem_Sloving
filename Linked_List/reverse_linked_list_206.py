# linked-list
# adobe | amazon | apple | bloomberg | facebook | microsoft | snapchat | twitter | uber | yahoo | yelp | zenefits
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prev=None
        while head:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev