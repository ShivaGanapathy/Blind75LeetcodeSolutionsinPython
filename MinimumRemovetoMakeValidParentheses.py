class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        
        for idx in stack:
            s[idx] = ""
            
                    
        return "".join(s)
        
