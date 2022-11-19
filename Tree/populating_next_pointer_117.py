# tree|breadth-first-search
# bloomberg|facebook|microsoft
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        q = deque()
        q.append(root)
        dummy = Node(-999)
        while (q):
            length = len(q)
            prev = dummy
            for i in range(length):
                cur = q.popleft()
                if cur.left:
                    prev.next=cur.left
                    prev = prev.next
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    prev.next = cur.right
                    prev = prev.next
        return root