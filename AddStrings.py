class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # Find the lengths of both strings
        i = len(num1) - 1 
        j = len(num2) - 1
        
        #carry will be used to keep track of the value that should be carried
        carry = 0
        #we will build our output string in an array
        result = []
        
        while i>=0 or j >=0:
            
            value = carry
            
            if i>=0:
                #This allows us to calculate the integer value using ASCII
                value += ord(num1[i]) - 48
                
            if j>=0:
                #This allows us to calculate the integer value using ASCII
                value += ord(num2[j]) - 48
                
            
            result.append(str(value%10))
            carry = value//10
            
            i -= 1
            j -= 1
            
        if carry != 0:
            result.append(str(carry))
            
        return "".join(result[::-1])
            
            
            
        
        
        
