class Solution:
    #O(n) Time Complexity
    #O(1) Space Complexity(Excluding the output array)
    def productExceptSelf(self, nums):
        output=[]
        
        prefix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
    
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
            
        return output
            

        