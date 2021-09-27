class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        
        def dfs(s):
            
            if s == "":
                return True
            cur = ""
            for idx, char in enumerate(s):
                cur += char
                if cur in wordDict:
                    
                    if s[idx+1:] not in memo :
                        memo[s[idx+1:]] = dfs(s[idx+1:])
                        
                    if memo[s[idx+1:]]:
                        return True
                    
            return False
        
        return dfs(s)
                    
        
