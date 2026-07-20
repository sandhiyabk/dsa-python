# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next #one step at a time
            fast=fast.next.next #two step at a time
            if slow==fast: #if it is cycle at any point of loop slow and fast will be equal
                return True
        return False
        
