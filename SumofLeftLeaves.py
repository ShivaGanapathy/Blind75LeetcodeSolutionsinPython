# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Recursively traverse the tree
        Pass in a boolean to determine if we are allowed to add to the sum
        Check if its a leaf node
        
        
        Input: root = [1]
        
        
        Input: [3,9,20,null,null,15,7]
        
        """
        if not root:
            return 0
        
        output = [0]
        
        def dfs(root,canSum):
            
            #check if its a leaf node
            if not root.left and not root.right:
                if canSum:
                    output[0] = output[0] + root.val
                    
            #traverse
            
            if root.left:
                dfs(root.left,True)
            if root.right:
                dfs(root.right,False)
            
        dfs(root,False)
        
        return output[0]
                