class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        
        while left<right:
            midpoint = left + (right-left)//2
            
            if (nums[midpoint]<nums[midpoint-1]):
                return nums[midpoint]
            
            elif (nums[left]<= nums[midpoint] and nums[midpoint] > nums[right]):
                left = midpoint + 1
            else:
                right = midpoint - 1
                    
        return nums[left]