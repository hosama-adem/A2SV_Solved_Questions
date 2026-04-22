# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, parent, grandparent):
            sum_nodes = 0

            if not node:
                return 0
            
            if grandparent and grandparent.val%2 == 0:
                sum_nodes += node.val
            
            sum_nodes += dfs(node.left, node, parent)
            sum_nodes += dfs(node.right, node, parent)
          
            return sum_nodes
        
        return dfs(root, None, None)
