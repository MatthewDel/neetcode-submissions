class LRUCache:

    def __init__(self, capacity: int):
        self.hash_nodes = {}
        self.start = None 
        self.tail = None
        self.capacity = capacity
        self.size = 0

    #This is fine
    def get(self, key: int) -> int:
        if key in self.hash_nodes:
            self.put(key, self.hash_nodes[key].value)
            return self.hash_nodes[key].value
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        #Case One: We need to update the node value and append it to the end of the doubly linked list
        #Case Two: We append a new node to the end. If the size exceeds the capacity, then we chop from the front
        #Case Three: Fence post. Nothing exists currently and we must address first case

        #Case Three--Since Easiest. This will always work because 1<= capacity <= 100
        if not self.start and not self.tail:
            node = LinkedNode(value, key)
            self.hash_nodes[key] = node 
            self.start = node 
            self.tail = node 
            self.size += 1 

        #Case One
        elif key in self.hash_nodes:
            #Three cases: node is the tail, node is the start, node is vanilla in the middle
            node = self.hash_nodes[key] 
            node.value = value
            if self.tail is not node:
                    
                if self.start is node:
                    node_next = node.next 
                    node_next.prev = None
                    self.start = node_next 
                    node.next = None
                    node.prev = self.tail
                    self.tail.next = node
                    self.tail = node
                else:
                    node.next.prev = node.prev 
                    node.prev.next = node.next
                    node.prev = self.tail 
                    node.next = None
                    self.tail.next = node 
                    self.tail = node


        #Case One 
        else:
            #Two Cases: Size is at capacity and size is not 
            node = LinkedNode(value, key)
            self.hash_nodes[key] = node 
            self.tail.next = node
            node.prev = self.tail 
            self.tail = node 
            if self.size == self.capacity: 
                del self.hash_nodes[self.start.key]
                self.start = self.start.next
                self.start.prev = None 
            else:
                self.size += 1



class LinkedNode:
    def __init__(self, value, key):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key
