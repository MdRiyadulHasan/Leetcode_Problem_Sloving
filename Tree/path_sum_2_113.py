# tree | depth-first-search
# bloomberg
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        res = []
        path = []
        path_sum=0
        self.dfs(root,targetSum,path_sum,res,path)
        return res
    def dfs(self,root,targetSum,path_sum,res,path):
        if not root:
            return 
        path_sum+=root.val
        path.append(root.val)
        if not root.left and not root.right and targetSum==path_sum:
            res.append(path[:])
        self.dfs(root.left,targetSum,path_sum,res,path)
        self.dfs(root.right,targetSum,path_sum,res,path)
        path.pop()