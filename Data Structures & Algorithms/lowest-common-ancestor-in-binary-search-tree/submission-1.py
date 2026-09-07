# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        

        paths = []

        def dfs(root, path, node, height):
            
            if root is None:
                return 0 

            path.append((height, root))

            if root == node:
                paths.append(path[:]) 

            if root.left:
                dfs(root.left, path, node, height+1)
            
            if root.right:
                dfs(root.right, path, node, height+1)

            path.pop()
            return

        dfs(root, [], p, 0)
        dfs(root, [], q, 0)

        lcaNode = None
        max_height = float("-inf")

        common_roots = set(paths[0]).intersection(set(paths[1]))

        for height, node in list(common_roots):

            if height > max_height:
                max_height = height
                lcaNode = node

        return lcaNode

        