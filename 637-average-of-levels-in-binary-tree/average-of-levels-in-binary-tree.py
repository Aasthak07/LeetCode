# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop(self):
        if self.front == -1:
            return None

        x = self.q[self.front]
        self.front += 1

        if self.front == len(self.q):
            self.front = -1
            self.q = []

        return x

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        ans = []
        queue = Queue()
        queue.push(root)

        while queue.size() > 0:
            level_size = queue.size()
            level_sum = 0

            for _ in range(level_size):
                node = queue.pop()
                level_sum += node.val

                if node.left is not None:
                    queue.push(node.left)

                if node.right is not None:
                    queue.push(node.right)

            ans.append(level_sum / level_size)

        return ans