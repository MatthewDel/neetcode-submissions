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
        dummy = Node(-1)
        hash_map = {}
        lead = dummy
        trav = head 
        while trav:
            hash_map[trav] = Node(trav.val)
            lead.next = hash_map[trav]
            trav = trav.next 
            lead = lead.next 
        
        trav = head 
        lead = dummy.next 
        while trav:
            if trav.random is not  None:
                lead.random = hash_map[trav.random]
            lead = lead.next
            trav = trav.next
        
        return dummy.next