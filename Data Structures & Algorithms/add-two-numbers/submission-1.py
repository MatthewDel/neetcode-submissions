# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        trav =  dummy 
        while left and right:
            calc = (left.val + right.val + carry)
            carry =  calc // 10
            trav.next = ListNode(calc % 10)
            trav = trav.next
            left = left.next
            right = right.next 
        
        while left:
            calc = (left.val + carry)
            carry = calc // 10
            trav.next = ListNode(calc % 10)
            trav = trav.next
            left = left.next
        
        while right:
            calc = (right.val + carry)
            carry = calc // 10
            trav.next = ListNode(calc % 10)
            trav = trav.next
            right = right.next

        if carry != 0:
            trav.next = ListNode(carry)
        
        return dummy.next
    
        