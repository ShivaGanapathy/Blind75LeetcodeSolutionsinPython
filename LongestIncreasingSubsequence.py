class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #O(n^2)
        lengths = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    lengths[i] = max(lengths[i],lengths[j]+1)
                    
        return max(lengths)
    
    