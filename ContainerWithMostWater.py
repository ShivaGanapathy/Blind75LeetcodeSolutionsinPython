class Solution:
    # Brute Force O(n^2)
    def maxArea(self, height):
        output = -inf
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                output = max(output,(j-i) * min(height[i],height[j]))
        return output
    
    # Optimal O(n)
    def maxArea(self,height):
        output = -inf
        l = 0
        r = len(height)-1
        while(l<r):
            output = max(output,(r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        return output