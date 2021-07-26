class Solution:
    def kClosest(self, points,k):
        """
        Trivial Solution Using Builtin Sort Function and Custom Compare Function
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        """
        def compare(element):
            return element[0]**2 + element[1]**2
        points.sort(key=compare)
        return points[:k]

    def kClosest(self, points,k):
        """
        Heap Solution Using MaxHeap
        Time Complexity: O(nlogk)
        Space Complexity: O(1)
        """
    
        from heapq import heapify
        from heapq import heappush as push 
        from heapq import heappop as pop, heappushpop as pushpop
        
        maxHeap = []
        heapify(maxHeap)
        
        for i in range(len(points)):
            coordinate = points[i]
            compare_int = -1*(coordinate[0]**2 + coordinate[1]**2)
            item = [compare_int,coordinate[0],coordinate[1]]
            
            
            if i >= k:
                pushpop(maxHeap,item)
            else:
                push(maxHeap,item)
                
        output = []
        while maxHeap:
            output.append(maxHeap.pop()[1:])
        return output
        
                
            
    
        