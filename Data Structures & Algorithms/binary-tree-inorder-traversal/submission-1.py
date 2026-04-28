# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper([], root)

    def helper(self, arr, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return arr
        
        self.helper(arr, root.left)
        arr.append(root.val)
        self.helper(arr, root.right)
        
        return arr