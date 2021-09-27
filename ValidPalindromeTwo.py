class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        lp = 0
        rp = len(s) - 1
        
        
        while lp<rp:
            if s[lp] != s[rp]:
                return self.isValid(s,lp+1,rp) or self.isValid(s,lp,rp-1)
            lp +=1
            rp -= 1
        return True
    
    
    def isValid(self,s,lp,rp):
        
        while lp<rp:
            if s[lp] != s[rp]:
                return False
            
            lp += 1
            rp -= 1
            
        return True
    
        
