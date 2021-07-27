# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        res = [-inf]
        
        def dfs(root):
            
            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            #max if we can split?
            split_allowed = max(left+right,right,left,0)
            split_allowed += root.val
            res[0] = max(split_allowed,res[0])
            
            #Max if we can't split?
            no_split = max(left,right,0)
            no_split += root.val
            
            return no_split
        
        return max(dfs(root),res[0])