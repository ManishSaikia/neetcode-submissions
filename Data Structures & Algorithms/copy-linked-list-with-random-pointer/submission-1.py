"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyToOld={None:None}
        # First Pass
        curr=head
        while curr:
            copy=Node(curr.val)
            copyToOld[curr]=copy
            curr=curr.next
        # Second Pass
        curr=head
        while curr:
            copy=copyToOld[curr]
            copy.next=copyToOld[curr.next]
            copy.random=copyToOld[curr.random]
            curr=curr.next
        return copyToOld[head]
