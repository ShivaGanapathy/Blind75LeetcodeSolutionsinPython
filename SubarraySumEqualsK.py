class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Brute Force N^2 :(
        count = 0
        for lp in range(len(nums)):
            current_value = 0
            for rp in range(lp,len(nums)):
                current_value += nums[rp]
                if current_value == k:
                    count +=1
        
        return count

        hashmap = {0:1}
        current_sum = 0
        output = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum - k in hashmap:
                output += hashmap[current_sum-k]

            if current_sum not in hashmap:
                hashmap[current_sum] = 0

            hashmap[current_sum] +=1

        return output
            
    

        
                
            
                
            
        
