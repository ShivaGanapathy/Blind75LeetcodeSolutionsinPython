class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums,target,leftMost):
            
            lp = 0
            rp = len(nums) - 1
            i = -1
            
            while lp<=rp:
                mid = lp + (rp-lp)//2
                
                if nums[mid] == target:
                    if leftMost:
                        rp = mid - 1
                    else:
                        lp = mid + 1 
                        
                    i = mid
                    
                elif nums[mid] > target:
                    rp = mid - 1
                    
                else:
                    lp = mid + 1
                    
            return i
        
        
        left = binary_search(nums,target,True)
        right = binary_search(nums,target,False)
        
        return [left,right]
        
