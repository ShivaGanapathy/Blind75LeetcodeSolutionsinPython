class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0 
        
        #Recursive DFS
        def dfs(r,c):
            visited.add((r,c))
            directions = [(1,0),(0,-1),(-1,0),(0,1)]
            for direction in directions:
                    x = r + direction[0]
                    y = c + direction[1]
                    
                    is_valid_x = 0 <= x < rows
                    is_valid_y = 0 <= y < cols
                    
                    is_land = False
                    if is_valid_x and is_valid_y:
                        is_land = grid[x][y] == "1"
                    
                    is_not_visited = (x,y) not in visited
                    
                    if is_not_visited and is_land:
                        dfs(x,y)
            
        
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q:
                current_x,current_y = q.popleft()
                directions = [(1,0),(0,1),(0,-1),(-1,0)]
                for direction in directions:
                    x,y = current_x+direction[0], current_y+direction[1]
                    is_valid_x_coor = 0 <= x < rows
                    is_valid_y_coor = 0 <= y < cols
                    is_land = False
                    if is_valid_x_coor and is_valid_y_coor:
                        is_land = grid[x][y] == "1"
                    is_not_visited = (x,y) not in visited
                    if is_valid_x_coor and is_valid_y_coor and is_land and is_not_visited:
                        q.append((x,y))
                        visited.add((x,y))
                        
                    
                
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    print(r,c)
                    bfs(r,c)
                    islands +=1
                    
        return islands
                    
                
        