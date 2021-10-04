class Solution:
    def myAtoi(self, s: str) -> int:
        
        state = 0
        sign = 1
        numbers = {"1","2","3","4","5","6","7","8","9","0"}
        numeric = ""
        i = 0
        while i < len(s):
            
            #State 0: Waiting for sign or number
            if state == 0:
                if s[i] == " ":
                    pass
                elif s[i] == "-":
                    sign = -1
                    state = 1
                elif s[i] == "+":
                    sign = 1
                    state = 1
                elif s[i] in numbers:
                    numeric += s[i]
                    state = 2
                else:
                    return 0
                
                
                
            #State 1: Waiting for a number
            
            elif state == 1:
                if s[i] == " ":
                    return 0
                elif s[i] == "-":
                    return 0
                elif s[i] == "+":
                    return 0
                elif s[i] in numbers:
                    numeric += s[i]
                    state = 2
                else:
                    return 0
                
                
            
            
            #State 2: Waiting for more numbers
            
            elif state == 2:
                
                if s[i] in numbers:
                    numeric += s[i]
                else:
                    break
                
            i+=1
            
        if not numeric:
            return 0
        
        value = 0
        tens = 1
        numeric = numeric[::-1]
        
        for i in range(len(numeric)):
            value += (ord(numeric[i])-48)*tens
            tens *= 10
            
        if value*sign < -2147483648:
            return -2147483648
        elif value*sign > 2147483647:
            return 2147483647
        else:
            return value*sign
                
                
        
