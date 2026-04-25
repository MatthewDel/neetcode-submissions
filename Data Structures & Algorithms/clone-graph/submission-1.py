"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        hashmap = {}
        hashmap[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                hashmap[curr].neighbors.append(hashmap[neighbor])
        
        return hashmap[node]
        

