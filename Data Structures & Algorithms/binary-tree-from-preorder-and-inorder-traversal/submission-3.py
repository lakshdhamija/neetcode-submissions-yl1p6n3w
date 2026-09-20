# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i, v in enumerate(inorder): hashmap[v] = i # mapping of val to index for inorder
        preorderIdx = 0
        def helper(l, r):
            nonlocal preorderIdx
            if l > r: return None
            node = TreeNode(preorder[preorderIdx])
            inorderIdx = hashmap[preorder[preorderIdx]]
            preorderIdx += 1
            node.left = helper(l, inorderIdx - 1)
            node.right = helper(inorderIdx + 1, r)
            return node
        return helper(0, len(inorder) - 1)