class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self,root) -> int: 
        def dfs(root,sum):
            if not root:
                return 0
            sum = sum*10+root.val
            if not root.left and not root.right:
                return sum
            return dfs(root.left, sum) + dfs(root.right, sum)
        return dfs(root,0)
if __name__ == '__main__':
    root=TreeNode(4)
    root.left=TreeNode(9)
    root.left.left=TreeNode(5)
    root.left.right=TreeNode(1)
    root.right = TreeNode(0)
    ob= Solution()
    ans =ob.sumNumbers(root)
    print(ans)