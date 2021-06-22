class Solution:
    #O(N) Time Complexity
    #O(1) Space Complexity
    def maxSubArray(self, nums):
        maximum = -math.inf
        lp = rp = 0
        counter = 0
        
        for i in range(len(nums)):
            if counter <0:
                lp = rp
                counter = nums[lp]
                
            else:
                counter += nums[rp]
                
            if counter > maximum:
                maximum = counter
                
            rp +=1
        
        return maximum
        