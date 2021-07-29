# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder[0]:
            return None
        else:
            root_val = preorder[0]
            root = TreeNode(root_val)
            mid  = inorder.index(root_val)
            root.left = seld.buildTree(preorder[1:],inorder[1:mid+1])
            root.right = seld.buildTree(preorder[1:],inorder[mid+1:])
            