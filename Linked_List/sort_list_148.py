class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        p,slow,fast=None,head,head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None
        left_list = self.sortList(head)
        right_list = self.sortList(slow)
        return self.merge(left_list,right_list)
    def merge(self,l1,l2):
        dummy = ListNode(None)
        cur = dummy
        while l1 and l2:
            if l1.val <=l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
if __name__ =='__main__':
    head = ListNode(4)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    ob = Solution()
    ans = ob.sortList(head)
    cur = ans
    while cur:
        print(cur.val)
        cur =cur.next
   