# tree | depth-first-search | breadth-first-search
# amazon
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        res = []
        if not root:
            return None
        q=deque()
        q.append(root)
        while q:
            length = len(q)
            for i in range(length):
                cur = q.popleft()
                val = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(val)
        return res