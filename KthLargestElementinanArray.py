class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Solution 1: Sort and Index
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        """

        nums.sort(reverse=True)
        return nums[k-1]


    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Solution 2: Use a Min Heap with K elements
        Time Complexity: O(nlogk)
        Space Complexity: O(n)
        """

        from heapq import heapify, heappop as pop, heappush as push, heappushpop as pushpop
        minHeap = []
        heapify(minHeap)
        
        for i in range(len(nums)):
            item = nums[i]
            if i+1 > k:
                pushpop(minHeap,item)
            else:
                push(minHeap,item)
                
        return pop(minHeap)
    
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Solution 3: Use Quickselect algorithm
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
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
        
            
        
            
        
        
    
        