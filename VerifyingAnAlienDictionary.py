class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        key = {}
        
        for idx, char in enumerate(order):
            key[char] = idx
        
        
        
        def isSort(word1,word2,key)->bool :
            
            for i in range(len(word1)):
                if i >= len(word2):
                    return False
                
                if key[word1[i]] < key[word2[i]]:
                    return True
                
                if key[word1[i]] > key[word2[i]]:
                    return False
                
            return True
                
        
        for i in range(1,len(words)):
            prev = words[i-1]
            cur = words[i]
            
            if not isSort(prev,cur,key):
                return False
            
        return True
        
