class Solution:

    
    def findCircleNum(self, isConnected):
        provinces = 0 
        visited = set()   
        
        #Using Depth First Search
        def dfs(city):
            visited.add(city)
            for i in range(len(isConnected[city])):
                if isConnected[city][i] == 1 and i not in visited:
                    dfs(i)

        #Using Breadth First Search
        def bfs(city):
            q = collections.deque()
            visited.add(city)
            q.append(city)
            
            while q:   
                city  = q.popleft()
                visited.add(city)
                for i in range(len(isConnected[city])):
                    if isConnected[city][i] == 1 and i not in visited:
                        q.append(i)
            
                
          
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces +=1
                
                
                
        return provinces


                
            