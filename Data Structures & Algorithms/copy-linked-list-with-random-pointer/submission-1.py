"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deep_hash = {}
        if not head:
            return None
        trav = head
        while trav:
            if trav not in deep_hash:
                deep_hash[trav] = Node(trav.val)
            if trav.next:
                if trav.next not in deep_hash:
                    deep_hash[trav.next] = Node(trav.next.val)
                deep_hash[trav].next = deep_hash[trav.next]
            else:
                deep_hash[trav].next = None
            if trav.random:
                if trav.random not in deep_hash:
                    deep_hash[trav.random] = Node(trav.random.val)
                deep_hash[trav].random = deep_hash[trav.random]
            else:
                deep_hash[trav].random = None
            trav = trav.next
        
        return deep_hash[head]

                

