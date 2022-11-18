class Node:
    def __init__(self,val):
        self.val=val
        self.left = None
        self.right = None
class Solution:
    def isValidBst(self, root):
        def valid(root,left,right):
            if not root:
                return True
            if not(root.val<right and left<root.val):
                return False
            return valid(root.left,left,root.val) and valid(root.right,root.val,right)
        return valid(root,float('-inf'),float('inf'))
if __name__ == '__main__':
    root = Node(6)
    root.left=Node(4)
    root.left.left=Node(2)
    root.left.right = Node(5)
    root.left.left.left=Node(1)
    root.left.left.right = Node(3)
    root.right = Node(8)
    root.right.left=Node(7)
    root.right.left.left=Node(4)
    root.right.right=Node(9)
    ob=Solution()
    ans = ob.isValidBst(root)
    print(ans)
