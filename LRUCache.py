class ListNode():
    
    def __init__(self,key,value):
        self.prev = None
        self.next = None
        self.key = key
        self.val = value
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        
        
    def detach_node(self, node):
        after = node.next
        before = node.prev
        before.next = after
        after.prev = before
        
    
    
    def attach_to_head(self, node):
        first = self.head.next
        self.head.next = node
        first.prev = node
        node.prev = self.head
        node.next = first
    
    def evict_node(self):
        remove = self.tail.prev
        before = remove.prev
        before.next = self.tail
        self.tail.prev = before
        del self.cache[remove.key]
    
    
        
        
        

    def get(self, key: int) -> int:
        # Either it's in the cache or its not
        
        #If it is
        if key in self.cache:
            node = self.cache[key]
            self.detach_node(node)
            self.attach_to_head(node)
            return node.val
        #if its not
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #Either it's already in the cache or its not
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.detach_node(node)
            self.attach_to_head(node)
        else:
            node = ListNode(key,value)
            self.cache[key] = node
            self.attach_to_head(node)
            if len(self.cache) > self.capacity:
                self.evict_node()
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
