class Node:
    def __init__(self,val):
        self.val=val
        self.left = None
        self.right = None
class Solution:
    def flatten(self, root):
        def dfs(root):
            if not root:
                return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            if root.left:
                leftTail.right=root.right
                root.right = root.left
                root.left=None
            last = rightTail or leftTail or root
            return last
        dfs(root)
        while root.right:
            print(root.val)
            root=root.right
        print(root.val)
if __name__ == '__main__':
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(3)
    root.left.right=Node(4)
    root.right=Node(5)
    root.right.right= Node(6)
    ob=Solution()
    ans=ob.flatten(root)
    print(ans)