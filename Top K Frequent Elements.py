from heapq import heappush as push, heappushpop as pushpop, heappop as pop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        frequency = {}
        
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
                
            frequency[num] += 1
            
        heap = []
        
        for key, value in frequency.items():
            
            if len(heap) < k:
                push(heap,[value,key])
                
            else:
                pushpop(heap,[value,key])
                
                
            
        output = []
        
        while heap:
            item = pop(heap)
            output.append(item[1])
            
            
        return output
