# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        q = collections.deque()
        q.append((root,0))
        output = []
        while q:
            
            current_node,level = q.popleft()
            if level == len(output):
                output.append([])
            output[level].append(current_node.val)
            if current_node.left:
                q.append((current_node.left,level+1))
            if current_node.right:
                q.append((current_node.right,level+1))
                
            
                
        return output
        