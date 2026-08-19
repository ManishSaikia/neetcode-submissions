class Node:
    def __init__(self, key=0, value=0):
        self.key,self.val=key,value
        self.next,self.prev=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        # head = LRU and tail = MRU
        self.head,self.tail=Node(),Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        prev_node = self.tail.prev

        prev_node.next=node
        node.prev=prev_node

        self.tail.prev=node
        node.next=self.tail


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.cap:
            LRU = self.head.next
            self.remove(LRU)
            del self.cache[LRU.key]
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        
