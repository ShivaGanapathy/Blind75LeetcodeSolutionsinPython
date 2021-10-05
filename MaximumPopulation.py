class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        arr = []
        
        for log in logs:
            arr.append((log[0],True))
            arr.append((log[1],False))
            
        
       
        arr.sort(key = lambda x: (x[0], x[1]))
        
        curMax=  -inf
        count = 0
        year = arr[0][0]
        for item in arr:
            if item[1]:
                count += 1
            else:
                count -= 1
                
            if count > curMax:
                curMax = count
                year = item[0]
                
                
        return year
                
        
