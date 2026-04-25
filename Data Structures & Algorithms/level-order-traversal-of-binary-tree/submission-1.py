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
            return []
        q = deque()
        q.append(root)
        while q:
            temp_list = []
            for i in range(len(q)):
                temp = q.popleft()
                temp_list.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            sol.append(temp_list[::])
        return sol 

                