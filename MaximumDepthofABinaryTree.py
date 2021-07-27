# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        q = collections.deque()
        q.append((root,1))
        output = 1
        
        while q:
            node,count = q.popleft()
            if node == None:
                output = max(count-1,output)
            else:
                q.append((node.left,count+1))
                q.append((node.right,count+1))
                
        return output
        
        
        