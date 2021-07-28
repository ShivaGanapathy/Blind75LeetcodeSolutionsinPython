# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        output = []
        
        def dfs(root):
            if not root:
                output.append("X")
            else:
                output.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
                
            
            
        dfs(root)
        
        return ",".join(output)
            
            
        

    def deserialize(self, data):
        
        data = data.split(",")
        self.i = 0
        
        def dfs():
            if data[self.i] == "X":
                self.i+=1
                return None
            else:
                value = int(data[self.i])
                self.i +=1
                node = TreeNode(value)
                node.left = dfs()
                node.right= dfs()
                
                return node
                
        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))