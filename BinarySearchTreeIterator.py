# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.i = 0
        self.array = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.array.append(root.val)
            dfs(root.right)
            
        dfs(root)
            
        
            
        
        

    def next(self) -> int:
        self.i += 1
        return self.array[self.i-1]
        
        
        

    def hasNext(self) -> bool:
        
        return self.i < len(self.array)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
