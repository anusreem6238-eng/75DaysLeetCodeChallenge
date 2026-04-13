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
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # Move fast ahead by n steps
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches last node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove nth node from end
        slow.next = slow.next.next
        
        return dummy.next