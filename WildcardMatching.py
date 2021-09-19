class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(s,p):
            
            
            if s == "" and p == "":
                return True
            
            
            if s == "":
                
                for char in p:
                    if char != "*":
                        return False
                return True
                    
            if p == "":
                return False
            
            
                
            
            if p[0] == s[0]:
                return dfs(s[1:],p[1:])
            
            if p[0] == "?":
                return dfs(s[1:],p[1:])
            
            if p[0] == "*":
                found = False
                j = 0
                while j<=len(s):
                    found = found or dfs(s[j:],p[1:])
                    j +=1
                    
                if found:
                    return True
                
                else:
                    return False
                
            return False
                    
        return dfs(s,p)
        
