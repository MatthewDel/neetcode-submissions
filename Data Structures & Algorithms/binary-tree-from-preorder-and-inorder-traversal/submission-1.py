# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    preorder: [1,2,3,4]
    inorder: [2,1,3,4]
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder, inorder):
            if not preorder:
                return None

            index_of_root = inorder.index(preorder[0])

            root = TreeNode(preorder[0])
            left_preorder = preorder[1 : index_of_root + 1]
            left_inorder = inorder[:index_of_root]
            right_preorder = preorder[index_of_root + 1: ]
            right_inorder = inorder[index_of_root + 1:]

            root.left = helper(left_preorder, left_inorder)
            root.right = helper(right_preorder, right_inorder)
            return root
        
        return helper(preorder, inorder)