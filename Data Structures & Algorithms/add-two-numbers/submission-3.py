# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        dummyhead = curr

        carryout = 0
        while right and left:
            new_value = (left.val + right.val + carryout) % 10 
            carryout = (left.val + right.val + carryout) // 10
            left.val = new_value 
            curr.next = left
            curr = curr.next
            left = left.next 
            right = right.next 

        while left:
            new_value = (left.val + carryout) % 10 
            carryout = (left.val + carryout) // 10
            left.val = new_value 
            curr.next = left
            curr = curr.next
            left = left.next
        
        while right:
            new_value = (right.val + carryout) % 10 
            carryout = (right.val + carryout) // 10
            right.val = new_value 
            curr.next = right
            curr = curr.next
            right = right.next
        
        if carryout:
            curr.next = ListNode(carryout)
        
        return dummyhead.next

       


    
        