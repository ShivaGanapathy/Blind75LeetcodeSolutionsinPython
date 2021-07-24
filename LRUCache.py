class Node:
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def setNext(self,next):
        self.next = next
        
    def setPrev(self,prev):
        self.prev = prev
        
    def setValue(self,value):
        self.value = value
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(None,None)
        self.tail = Node(self.head,None)
        self.head.setNext(self.tail)
        

    def get(self, key: int) -> int:
        if key in self.cache:
            #deletes node from current place in list
            curNode = self.cache[key][1]
            prevNode = curNode.prev
            nextNode = curNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            
            #inserts node at head
            nextNode = self.head.next
            self.head.setNext(curNode)
            curNode.setPrev(self.head)
            curNode.setNext(nextNode)
            nextNode.setPrev(curNode)
            
            return self.cache[key][0]
            
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            nextNode = self.head.next
            curNode = Node(key,value)
            self.head.setNext(curNode)
            curNode.setPrev(self.head)
            curNode.setNext(nextNode)
            nextNode.setPrev(curNode)
            self.cache[key] = (value,curNode)
            self.size += 1
        
        else:
            curNode = self.cache[key][1]
            curNode.setValue(value)
            prevNode = curNode.prev
            nextNode = curNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            
            nextNode = self.head.next
            self.head.setNext(curNode)
            curNode.setPrev(self.head)
            curNode.setNext(nextNode)
            nextNode.setPrev(curNode)
            self.cache[key] = (value,curNode)
            
            
        
        
        if self.size > self.capacity:
            lruNode = self.tail.prev
            lruNode.prev.setNext(self.tail)
            self.tail.setPrev(lruNode.prev)
            del self.cache[lruNode.key]
            self.size -=1 
            
        