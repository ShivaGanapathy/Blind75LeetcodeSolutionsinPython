class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 0
        counter = 0
        output = 0
        visited = set()
        
        for rp, char in enumerate(s):
            while char in visited:
                rem_char = s[lp]
                visited.remove(rem_char)
                lp += 1
                counter -= 1
                
            visited.add(char)
            counter +=1
            output = max(output,counter)
            
            
        return output