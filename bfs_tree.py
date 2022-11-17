class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right = None
class Solution:
    def pathSum(self, root, sum: int):
        self.res = []
        self.dfs(root, sum, 0, [])
        return self.res
            
    def dfs(self, root, target:int, prev_sum:int, my_list:list):
        if not root:
            return
        prev_sum += root.val
        my_list.append(root.val)
       
        if prev_sum == target and root.left == None and root.right == None:
            self.res.append(my_list[:])
        
        self.dfs(root.left, target, prev_sum, my_list)
        self.dfs(root.right, target, prev_sum, my_list)
        my_list.pop()

if __name__ =="__main__":
    root=Node(5)
    root.left = Node(4)
    root.left.left=Node(11)
    root.left.left.left=Node(7)
    root.left.left.right=Node(2)
    root.right = Node(8)
    root.right.left=Node(13)
    root.right.right = Node(4)
    root.right.right.left=Node(5)
    root.right.right.right=Node(1)
    ob=Solution()
    #root = [5,4,8,11,None,13,4,7,2,None,null,null,1]
    ans=ob.pathSum(root,22)
    print(ans)
