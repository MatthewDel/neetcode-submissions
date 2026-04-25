# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 1

        while curr.next:
            curr = curr.next 
            length += 1

        index_to_find = length // 2
        index = 0
        curr = head

        while index != index_to_find:
            curr = curr.next
            index += 1
        
        reversed_list = self.reverse(curr.next)
        curr.next = None

        dummy = ListNode(-1)
        curr = dummy 

        while reversed_list and head:
            curr.next = head
            head = head.next 
            curr.next.next = reversed_list
            reversed_list = reversed_list.next
            curr = curr.next.next
        
        if reversed_list:
            curr.next = reversed_list
        elif head:
            curr.next = head



        

        
