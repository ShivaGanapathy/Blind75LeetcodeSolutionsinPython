class TreeNode():
    def __init__(self,val):
        self.val = val
        self.children = []



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Input: "23"
        Input : ""
    
        
    
    
    
    
    
    
        """
        if digits == "":
            return []
        
        output = []
        hashmap = {
            1 : [],
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"]
        }
        root = TreeNode("")
        
        
        
        def buildTree(root,digits):
            
            if not root:
                return
            
            if not string or len(digits)==0:
                output.append(root.val)
                return
            
            
            current_digit = int(digits[0])
            possible_letter = hashmap[current_digit]
            
    
            for letter in possible_letter:
                current_child = TreeNode(root.val+letter)
                root.children.append(current_child)
                buildTree(current_child,digits[1:])
            
            
        buildTree(root,digits)
        
        
        return output
            