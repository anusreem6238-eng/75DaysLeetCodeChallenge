# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
            
        pA = headA
        pB = headB
        
        # Loop until pA and pB point to the exact same node reference.
        # If no intersection exists, both will hit None at the same time.
        while pA != pB:
            # If pA reaches the end of List A, switch it to Head B. 
            # Otherwise, just move to the next node.
            pA = pA.next if pA else headB
            
            # If pB reaches the end of List B, switch it to Head A.
            # Otherwise, just move to the next node.
            pB = pB.next if pB else headA
            
        return pA