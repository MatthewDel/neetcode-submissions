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
        hashOldToNew = {}
        self.copy(hashOldToNew, head)
        return hashOldToNew[head]

        

    def copy(self, hashOldToNew, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            hashOldToNew[head] = None
            return None
        
        curr = hashOldToNew[head] if head in hashOldToNew else Node(head.val, None, None)
        hashOldToNew[head] = curr

        if not curr.random and head.random:
            if head.random in hashOldToNew:
                curr.random = hashOldToNew[head.random]
            else:
                curr.random = Node(head.random.val, None, None)
                hashOldToNew[head.random] = curr.random

        if not curr.next and head.next:
            if head.next in hashOldToNew:
                curr.next = hashOldToNew[head.next]
            else:
                curr.next = Node(head.next.val, None, None)
                hashOldToNew[head.next] = curr.next
        
        return self.copy(hashOldToNew, head.next)