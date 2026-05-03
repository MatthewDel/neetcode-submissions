# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []

        if not root:
            return sol 
            
        queue = deque([root])
        while queue:
            temp = []
            starting_length = len(queue)
            
            for i in range(starting_length):
                popped = queue.popleft()
                temp.append(popped.val)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)

            print(temp)
            print(queue)
            sol.append(temp)
        
        return sol
