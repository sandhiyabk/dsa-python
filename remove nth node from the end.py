# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to easily handle removing the head node
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move the fast pointer n + 1 steps forward
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        # Delink the nth node from the end
        slow.next = slow.next.next
        
        # Return the actual head of the modified list-because dummy.next is head it holds the address of the head node
        return dummy.next
