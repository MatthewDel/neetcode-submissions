# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = [] 

        def dfs(root):
            nonlocal serialized

            if not root:
                serialized.append("N")
                return
            
            serialized.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(serialized)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        index = 0
        data = data.split(',')
        def helper():
            nonlocal index 

            if index >= len(data) or data[index] == 'N':
                index += 1
                return None
            
            toReturn = TreeNode(data[index])
            index += 1
            toReturn.left = helper()
            toReturn.right = helper()

            return toReturn

        return helper()
