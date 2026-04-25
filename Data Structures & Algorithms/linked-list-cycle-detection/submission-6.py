# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        tortois = head 
        heir = head.next

        while heir and heir.next:
            if tortois == heir:
                return True
            tortois = tortois.next
            heir = heir.next.next
        
        return False

        