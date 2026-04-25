# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        sol = []
        q = deque()
        q.append(root)

        while q:
            temp = []
            for i in range(len(q)):
                trav = q.popleft()
                temp.append(trav.val)
                if trav.left:
                    q.append(trav.left)
                if trav.right:
                    q.append(trav.right)
            sol.append(temp)
        return sol
