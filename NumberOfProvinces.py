class Solution:

    #Using Depth First Search
    def findCircleNum(self, isConnected):
        provinces = 0 
        visited = set()   
        
        def dfs(city):
            visited.add(city)
            for i in range(len(isConnected[city])):
                if isConnected[city][i] == 1 and i not in visited:
                    dfs(i)
            
                
          
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces +=1
                
                
                
        return provinces
                
            