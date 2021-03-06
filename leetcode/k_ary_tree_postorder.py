# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# https://leetcode.com/articles/n-ary-tree-postorder-transversal  (Premium)


# runtime: 100 ms, 39%; memory 17.5 MB, 6%
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []

        def _traverse(node):
            if node:
                if node.children:
                    for kid in node.children:
                        _traverse(kid)
                res.append(node.val)

        _traverse(root)
        return res


# runtime 104 ms, 21%; memory 17.4 MB, 6%
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.insert(0, curr.val)
            stack += curr.children
        return res


# sample 84 ms submission. when i ran, i got:
# runtime 100 ms, 39%; 17.6 MB, 6%
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack += node.children
        return ans[::-1]
