class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        s = []
        
        i = len(a)-1
        j = len(b)-1
        hashmap = {"0":0,"1":1}
        carry = 0
        while i>=0 or j>=0:
            
            value = carry
            
            if i>=0:
                value += hashmap[a[i]]
            if j>=0:
                value += hashmap[b[j]]
                
            carry = value//2
            value -= carry*2
            
            s.append(str(value))
            
            i -= 1
            j -= 1
            
        if carry != 0:
            s.append("1")
            
            
        return "".join(s[::-1])
                
                
        
