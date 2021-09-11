class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix)>0 and len(matrix[0])>0:
            output = [matrix[0][0]]
        else:
            output = []
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        
        
        
        def dfs(index, pointer):
            x,y = index
            
            
            
            
            for i in range(0,4):
                curX, curY = x + directions[pointer][0], y + directions[pointer][1]
                if 0 <= curX < len(matrix) and  0 <= curY < len(matrix[0]) and (curX,curY) not in visited:
                    output.append(matrix[curX][curY])
                    visited.add((curX,curY))
                    dfs((curX,curY),pointer)
                    break
                pointer += 1
                pointer = pointer % 4
        
        
        visited.add((0,0))
        dfs((0,0),0)
        return output
            
