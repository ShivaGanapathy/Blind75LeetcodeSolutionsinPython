def hasCycle(self, head: ListNode) -> bool:
        
        # O(n) time complexity
        # O(n) space complexity
        
        
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                
            head= head.next
            
            
        return False


        
        
        
     
    # O(n) time complexity
    # O(1) space complexity
def hasCycle(self, head: ListNode) -> bool:
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False