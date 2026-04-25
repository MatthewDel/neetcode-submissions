# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1 
            temp = temp.next 
        
        location = count - n
        
        temp = head 
        count = 0

        if location == 0:
            return head.next
        while temp:
            count += 1
            if count == location:
                temp.next = temp.next.next
                return head
            temp = temp.next
        

    