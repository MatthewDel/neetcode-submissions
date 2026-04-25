# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        heir = head
        while heir.next and heir.next.next:
            tortoise = tortoise.next
            heir = heir.next.next
            if tortoise == heir:
                return True
        return False
