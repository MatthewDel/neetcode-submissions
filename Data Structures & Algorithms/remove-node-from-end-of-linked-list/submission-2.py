# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        running_length = 0
        while curr:
            running_length += 1
            
            if (length - running_length + 1) == n:
                prev.next = curr.next 
                return dummy.next
            
            prev = curr
            curr = curr.next
        
        return dummy.next

        



