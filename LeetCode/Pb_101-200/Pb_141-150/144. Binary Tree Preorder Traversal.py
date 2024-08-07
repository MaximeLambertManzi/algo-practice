""" Given the root of a binary tree,
return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively? """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trav(self, root, pre_trav):
        if root:
            pre_trav.append(root.val)
            self.trav(root.left, pre_trav)
            self.trav(root.right, pre_trav)
        else:
            return 0

    def preorderTraversal(self, root):
        pre_trav = []

        self.trav(root, pre_trav)

        return pre_trav
