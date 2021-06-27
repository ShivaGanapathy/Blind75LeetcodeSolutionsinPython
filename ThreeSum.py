class Solution:
    def threeSum(self, nums):
        nums.sort()
        output = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            
            while (left<right):
                currentSum = nums[left] + nums[right] + nums[i]
                if currentSum == 0:
                    output.append([nums[i],nums[left],nums[right]])
                    left +=1
                    while nums[left] == nums[left-1] and left<right:
                        left +=1
                
                elif currentSum>0:
                    right -=1
                else:
                    left +=1
        return output
        
        