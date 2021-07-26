class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        
        Three solutions:
        - Sort and return
        - Use a Heap
        - Quickselect
        
        """
        
        #Solution #1: Sort
        # nums.sort(reverse=True)
        # return nums[k-1]
        
        
        #Solution #2: Use a Min Heap
#         from heapq import heapify,heappop as pop,heappush as push
#         from heapq import heappushpop as pushpop
        
#         minHeap = []
#         heapify(minHeap)
        
#         for i in range(len(nums)):
#             item = nums[i]
#             if i+1 > k:
#                 pushpop(minHeap,item)
#             else:
#                 push(minHeap,item)
                
#         return pop(minHeap)
    
        
        #Solution #3 Using the quickselect algorithm
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x==pivot]
        right = [x for x in nums if x < pivot]
        
        left_length = len(left)
        mid_length = len(mid)
        
        if k <= left_length:
            return self.findKthLargest(left,k)
        elif k > (mid_length + left_length):
            return self.findKthLargest(right,k-(mid_length+left_length))
        else:
            return mid[0]
        
            
        
            
        
        
    
        