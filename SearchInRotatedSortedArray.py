class Solution:
    def search(self, nums, target):
        left,right = 0,len(nums)-1
        
        while (left<=right):
            midpoint = left + (right-left)//2
            
            if nums[midpoint] == target:
                return midpoint
            
            #If we are in the left sorted array
            if nums[midpoint] >= nums[left]:
                if target > nums[midpoint]:
                    left = midpoint + 1
                elif target < nums[left]:
                    left = midpoint + 1
                else:
                    right = midpoint - 1
                
            #right sorted portion of the array
            else:
                if target > nums[right]:
                    right = midpoint - 1
                elif target < nums[midpoint]:
                    right = midpoint - 1
                else:
                    left = midpoint + 1
                
        return -1
