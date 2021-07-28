# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def dfs(root,minimum,maximum):
            
            if not root:
                return True
            if minimum < root.val < maximum:
                c1 = dfs(root.left,minimum,root.val)
                c2 = dfs(root.right,root.val,maximum)
                return c1 and c2
            else:
                return False
        
        return(dfs(root,-inf,inf))
        
        
                
        
        
        
            
        