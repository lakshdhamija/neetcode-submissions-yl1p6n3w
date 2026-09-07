# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        def dfs(node):
            if not node: return [False, False]
            if self.res: return [True, True]
            [pFoundLeft, qFoundLeft] = dfs(node.left)
            [pFoundRight, qFoundRight] = dfs(node.right)
            if not self.res and (node == p or pFoundLeft or pFoundRight) and (node == q or qFoundLeft or qFoundRight):
                self.res = node
                return [True, True]
            return [(node == p or pFoundLeft or pFoundRight), (node == q or qFoundLeft or qFoundRight)]
        dfs(root)
        return self.res