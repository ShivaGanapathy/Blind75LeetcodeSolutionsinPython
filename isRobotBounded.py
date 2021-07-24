class Solution:
    #O(n) time complexity
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0
        
        for instruction in instructions:
            if instruction == "G":
                x += directions[d%4][0]
                y += directions[d%4][1]
            elif instruction == "L":
                d -= 1
            elif instruction == "R":
                d += 1
                
        condition1 = x == 0 and y == 0
        condition2 = d%4 != 0 
        
        return condition1 or condition2