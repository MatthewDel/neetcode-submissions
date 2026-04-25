# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tortoise =  head
        heir = head.next

        while heir and heir.next:
            tortoise = tortoise.next
            heir = heir.next.next

        curr = tortoise.next
        tortoise.next = None

        prev = None 
        
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 

        dummy = ListNode()
        curr = dummy
        while prev and head:
            curr.next = head
            head = head.next
            curr = curr.next
            curr.next = prev
            prev = prev.next
            curr = curr.next
        
        curr.next = head
        
    

        