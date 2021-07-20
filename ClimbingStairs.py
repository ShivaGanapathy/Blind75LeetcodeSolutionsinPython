class Solution:
    #Recursive Solution: 2^n
    def climbStairs(self, n):
        if n<2:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    #Bottom Up Solution: #O(N) Time Complexity & O(N) Space Complexity
    def climbStairs(self,n):
        array = [1,1]
        for i in range(2,n+1):
            array.append(array[i-1] + array[i-2])
        return array[n]
    
    #Bottom Up Solution: #O(N) Time Complexity & O(1) Space Complexity
    def climbStairs(self,n):
        first, second = 1,1
        for i in range(2,n+1):
            temp = first
            first = second
            second = temp + first
        return second
    
    