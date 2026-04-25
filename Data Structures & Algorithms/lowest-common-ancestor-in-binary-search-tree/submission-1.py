# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        max_value = max(p.val, q.val)
        min_value = min(p.val, q.val)
        if root.val == p.val or root.val == q.val or (min_value < root.val < max_value):
            return root
        if max_value < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right,p, q)
        
        