# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr.next = l1
        overflow = 0

        while l1 and l2:
            computation = (l1.val + l2.val + overflow)
            l1.val = computation % 10
            overflow = math.floor(computation / 10)

            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1 and overflow != 0:
            computation = (l1.val + overflow)
            l1.val = computation % 10
            overflow = math.floor(computation / 10)
            l1 = l1.next
            curr = curr.next


        if l2:
            curr.next = l2

        while l2 and overflow != 0:
            computation = (l2.val + overflow)
            l2.val = computation % 10
            overflow = math.floor(computation / 10)
            l2 = l2.next
            curr = curr.next
        
        if overflow != 0:
            curr.next = ListNode(overflow)
            
        return dummy.next


        