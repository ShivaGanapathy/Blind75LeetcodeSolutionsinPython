class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def setNext(self,nextNode):
        self.next = nextNode
    def setPrev(self,prevNode):
        self.prev = prevNode
    def setValue(self,value):
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.setNext(self.tail)
        self.head.setPrev(self.head)
        
    def deleteNode(self,curNode):
        prevNode = curNode.prev
        nextNode = curNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size-=1
    
    def insertNode(self,curNode):
        nextNode = self.head.next
        self.head.next = curNode
        curNode.prev = self.head
        curNode.next = nextNode
        nextNode.prev = curNode
        self.size+=1
        
    

    def get(self, key: int):
        if key in self.cache:
            curNode = self.cache[key][1]
            self.deleteNode(curNode)
            self.insertNode(curNode)
            return self.cache[key][0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #push the key node to the head
            curNode = self.cache[key][1]
            self.deleteNode(curNode)
            self.insertNode(curNode)
            #update value at index key
            self.cache[key][0] = value
            
        else:
            curNode = Node(key,value)
            self.insertNode(curNode)
            self.cache[key] = [value,curNode]
            
            
        if self.size > self.capacity:
            #get rid of lru
            lruNode = self.tail.prev
            self.deleteNode(lruNode)
            del self.cache[lruNode.key]
        

