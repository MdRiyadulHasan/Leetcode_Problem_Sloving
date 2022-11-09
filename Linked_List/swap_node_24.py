# linked-list
# bloomberg | microsoft | uber
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs( head):
    dummy = ListNode(0, head)
    prev=dummy
    cur=head
    while cur and cur.next:
        nxtpair=cur.next.next
        second=cur.next
        # reverse
        second.next=cur
        cur.next=nxtpair
        prev.next=second
        # update
        prev=cur
        cur=nxtpair
    return dummy.next