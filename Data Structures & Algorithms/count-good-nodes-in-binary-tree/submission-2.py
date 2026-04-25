# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def good_nodes(max_value, root):
            if not root:
                return 
            if root.val >= max_value:
                nonlocal count
                count = count + 1
            max_value = max(max_value, root.val)
            good_nodes(max_value, root.left)
            good_nodes(max_value, root.right)

        good_nodes(float('-inf'), root)
        return count
            