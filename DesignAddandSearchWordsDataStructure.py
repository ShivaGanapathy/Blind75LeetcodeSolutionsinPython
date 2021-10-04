

class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            
            current_node = current_node.children[char]
            
        current_node.word = True
        
        
        

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in root.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                
                else:
                    if char not in root.children:
                        return False
                    root = root.children[char]
                    
            return root.word
        
        
        return dfs(0,self.root)
                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
