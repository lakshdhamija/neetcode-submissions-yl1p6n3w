# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i, v in enumerate(inorder): hashmap[v] = i
        preorderIndex = 0
        def helper(l, r):
            nonlocal preorderIndex
            if l > r: return None
            node = TreeNode(preorder[preorderIndex])
            inorderRootIndex = hashmap[preorder[preorderIndex]]
            preorderIndex += 1
            node.left = helper(l, inorderRootIndex - 1)
            node.right = helper(inorderRootIndex + 1, r)
            return node
        return helper(0, len(inorder) - 1)
