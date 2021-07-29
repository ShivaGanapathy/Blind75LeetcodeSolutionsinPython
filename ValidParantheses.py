class Solution:
    def isValid(self, s: str) -> bool:
        
        #O(n) time complexity
        #O(n) space complexity
        
        stack = []
        hashmap = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        for char in s:
            if char in hashmap:
                stack.append(hashmap[char])
                
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False
                
        if len(stack) >0:
            return False
            
        return True
            
            
                
            
        
        