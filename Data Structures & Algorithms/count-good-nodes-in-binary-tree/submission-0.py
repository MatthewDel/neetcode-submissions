# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0 
        def check(root, max_value):
            if not root:
                return 
            if root.val >= max_value:
                self.count += 1
            new_value = max(max_value, root.val)
            check(root.left, new_value)
            check(root.right, new_value)
        check(root, float('-inf'))
        return self.count