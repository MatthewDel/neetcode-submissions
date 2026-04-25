# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        tortoise = dummy
        heir = head
        while heir.next and heir.next.next:
            if tortoise == heir:
                return True
            tortoise = tortoise.next
            heir = heir.next.next
        return False
