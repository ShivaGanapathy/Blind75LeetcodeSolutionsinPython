class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        #approach 1: Add all valid chars to a list and reverse
        #O(n) space and time complexity :(
        
        chars = []
        for char in s:
            if char.isalnum():
                if char.isalpha():
                    chars.append(char.lower())
                else:
                    chars.append(char)
                
        
        return chars == chars[::-1]
    
    

        #approach 2: two pointers
        # O(n) time, O(1) space :)
        lp = 0
        rp = len(s) - 1
        
        while lp<rp:
        
            if not s[lp].isalnum():
                lp +=1
            elif not s[rp].isalnum():
                rp -= 1
            else:
                left_char = s[lp]
                right_char = s[rp]

                if left_char.isalpha():
                    left_char = left_char.upper()

                if right_char.isalpha():
                    right_char = right_char.upper()

                if left_char != right_char:
                    return False

                lp +=1 
                rp -=1
        return True
                
            
            
        
