# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(root):
            if not root:
                return []
            output = []
            q = collections.deque()
            q.append((1,root))
            level = 1
            prevNode = None
            while q:
                l,node = q.popleft()
                if node.left:
                    q.append((l+1,node.left))
                if node.right:
                    q.append((l+1,node.right))
                    
                if l != level:
                    output.append(prevNode.val)
                    level = l
                
                prevNode = node
                
            output.append(prevNode.val)
            return output
                
        return bfs(root)
                
                    
                
                
            
            
