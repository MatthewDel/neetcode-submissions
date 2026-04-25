# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        sol = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                trav = q.popleft()
                if i == n-1:
                    sol.append(trav.val)
                if trav.left:
                    q.append(trav.left)
                if trav.right:
                    q.append(trav.right)
        return sol