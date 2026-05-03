# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        if not root:
            return sol
        
        queue = deque([root])
        while queue:
            original_length = len(queue)
            for i in range(original_length):
                popped = queue.popleft()
                if i == (original_length - 1):
                    sol.append(popped.val)
                
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                
        return sol 
