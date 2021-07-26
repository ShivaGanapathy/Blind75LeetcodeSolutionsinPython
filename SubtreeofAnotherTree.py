# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        
        if root == None:
            return False
        elif self.isSame(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
    def isSame(self,s,r):
        
        if s == None or r == None:
            return s == None and r == None
        elif s.val == r.val:
            return self.isSame(s.left,r.left) and self.isSame(s.right,r.right)
        else:
            return False
        
        
        