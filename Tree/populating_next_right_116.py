# tree | breadth-first-search
# microsoft
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root ):
        if not root:
            return 
        q = deque()
        q.append(root)
        while (q):
            cur=q.popleft()
            if cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next=cur.next.left
                q.append(cur.left)
                q.append(cur.right)
        return root