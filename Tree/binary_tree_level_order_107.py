from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(root):
        if root is None:
            return root
        res = []
        q = deque()
        q.append(root)
        while(len(q)>0):
            level = []
            l = len(q)
            for i in range(l):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return reversed(res)