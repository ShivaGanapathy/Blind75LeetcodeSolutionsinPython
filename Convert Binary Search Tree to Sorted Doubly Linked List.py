class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    
    def dfs(self, node):
        if node:
            self.dfs(node.left)
        	
            if self.first is None: 
                self.first = node
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            self.prev = node
                      
            self.dfs(node.right)
    
    def treeToDoublyList(self, root):
        if not root: 
            return root
        self.first = None
        self.prev = None
        self.dfs(root)
        self.first.left = self.prev
        self.prev.right = self.first  
        return self.first
