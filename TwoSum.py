class Solution:
    # O(n^2) Time Complexity
    #Brute Force Method
    def twoSum1(self,nums,target):
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            for j in range(i+1,len(nums)):
                if nums[j] == complement:
                    return [i,j]
    
    # O(n) Time Complexity
    # Hashmap Smart Method
    def twoSum2(self,nums,target):
        values={}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in values:
                return [values[complement],i]
            else:
                values[current] = i
                
            
            
        