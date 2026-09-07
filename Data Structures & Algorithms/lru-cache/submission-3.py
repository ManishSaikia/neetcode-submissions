class Node:
    def __init__(self, key=0, value=0):
        self.key,self.val=key,value
        self.next=self.prev=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}

        # Left = MRU , right = LRU
        self.left, self.right= Node(), Node()
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def insert(self, node):
        prevNode=self.right.prev

        node.prev=prevNode
        prevNode.next=node

        node.next=self.right
        self.right.prev=node

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
            LRU=self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        node=Node(key,value)
        self.cache[key]=node
        self.insert(node)
