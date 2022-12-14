class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
if __name__ == '__main__':
    preorder = [3,9,20,15,7] 
    inorder = [9,3,15,20,7]
    ob = Solution()
    ans =ob.buildTree(preorder,inorder)
    print(ans)