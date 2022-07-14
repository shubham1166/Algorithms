# Given the root of a binary tree, return the preorder traversal of its nodes' values.

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return res



        