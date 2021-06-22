class Solution:
    # O(nlogn) Time Complexity
    # O(1) Space Complexity
    def containsDuplicate1(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                return True
        return False
    
    #O(n) Time Complexity
    #O(n) Space Complexity
    def containsDuplicate2(self,nums):
        vals = set()
        for value in nums:
            if value in vals:
                return True
            else:
                vals.add(value)
        return False
    
    
        