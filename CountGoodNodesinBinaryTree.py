def goodNodes(self, root: TreeNode) -> int:
        
        
        """
        O(n) time complexity
        O(n) space complexity
        """
        
        output = [0]
        def dfs(root, current_max):
            if not root:
                return
            
            if root.val >= current_max:
                output[0] += 1
            
            current_max = max(current_max,root.val)
                
                
            dfs(root.left,current_max)
            dfs(root.right,current_max)
            
            
        dfs(root,root.val)