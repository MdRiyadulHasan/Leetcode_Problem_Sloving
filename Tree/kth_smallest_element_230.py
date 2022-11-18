# binary-search | tree
# bloomberg | google | uber
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k: int) :
        stack = []
        n = 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            n = n+1
            if n == k:
                return root.val
            root = root.right