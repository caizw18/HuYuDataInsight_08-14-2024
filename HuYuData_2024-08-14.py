class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node):
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root

# Example usage:
# root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
# sol = Solution()
# sol.connect(root)
# # The next pointers are now populated.