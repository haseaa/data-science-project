# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queueRoot = collections.deque()
        queueLevel = collections.deque()
        queueRoot.append(root)
        queueLevel.append(0)
        right = []
        while len(queueRoot) != 0:
            current = queueRoot.popleft()
            level = queueLevel.popleft()
            if current and len(right) == level:
                right.append(current.val)
            if current and current.right:
                queueRoot.append(current.right)
                queueLevel.append(level+1)
            if current and current.left:
                queueRoot.append(current.left)
                queueLevel.append(level+1)
        return right
        