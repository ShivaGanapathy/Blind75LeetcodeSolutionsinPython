class Solution:
    #O(n^2)
    def maxProduct(self, nums):
        maximum = -inf
        for i in range(len(nums)):
            counter = nums[i]
            if counter > maximum:
                maximum = counter
            for j in range(i+1,len(nums)):
                counter *= nums[j]
                if counter > maximum:
                    maximum = counter
        return maximum
    
    #O(n) time complexity
    def maxProduct(self,nums):
        maxi = 1 
        mini = 1
        output = max(nums)
        for i in range(len(nums)):
            temp = maxi*nums[i]
            maxi = max(maxi*nums[i],mini*nums[i],nums[i])
            mini = min(temp,mini*nums[i],nums[i])
            output = max(maxi,output)
        return output