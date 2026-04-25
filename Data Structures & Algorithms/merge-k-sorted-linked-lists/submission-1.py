# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] 
        count = 0
        for node in range(len(lists)):
            trav = lists[node]
            while trav:
                count += 1
                heapq.heappush(heap, (trav.val, count, trav))
                trav = trav.next 
        print(heap)
        
        dummy = ListNode()
        trav = dummy
        while heap:
            trav.next = heapq.heappop(heap)[2]
            trav = trav.next
        return dummy.next