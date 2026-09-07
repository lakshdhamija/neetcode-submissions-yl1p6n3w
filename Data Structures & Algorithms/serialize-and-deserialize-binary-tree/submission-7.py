# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        res = []
        def dfs(node):
            if not node: 
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        vals, self.i = data.split(','), 0
        def dfs():
            val = vals[self.i]
            if val == 'N':
                self.i += 1
                return None
            node = TreeNode(int(val))
            self.i += 1
            if self.i == 1: self.root = node
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()