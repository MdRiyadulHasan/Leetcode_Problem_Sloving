class Node:
    def __init__(self,val):
        self.val=val
        self.left = None
        self.right = None
class Solution:
    def preorder(self,root):
        if not root:
            return
       
        self.preorder(root.left)
        print(root.val)
        self.preorder(root.right)
if __name__ == '__main__':
    root=Node(25)
    root.left=Node(15)
    root.left.left=Node(10)
    root.left.right=Node(22)
    root.left.left.left=Node(4)
    root.left.left.right=Node(12)
    root.left.right.left=Node(18)
    root.left.right.right=Node(24)
    root.right=Node(50)
    root.right.left=Node(35)
    root.right.left.left=Node(31)
    root.right.left.right=Node(44)
    root.right.right=Node(70)
    root.right.right.left=Node(66)
    root.right.right.right=Node(90)
    ob=Solution()
    ans=ob.preorder(root)
    print(ans)
