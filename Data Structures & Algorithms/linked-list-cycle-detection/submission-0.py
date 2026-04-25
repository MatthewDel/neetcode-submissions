# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        heir = head.next
        while heir and heir.next and heir.next.next:
            if turtle == heir:
                return True
            turtle = turtle.next
            heir = heir.next.next 
        return False