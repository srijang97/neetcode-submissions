# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0

        def dfs(root, curr_depth):
            nonlocal depth

            if root is None:
                return
                
            if root.left is None and root.right is None:
                depth = max(depth, curr_depth)

            if root.left:
                dfs(root.left, curr_depth + 1)
            if root.right:
                dfs(root.right, curr_depth + 1)

            return

        dfs(root, 1)

        return depth

            
        