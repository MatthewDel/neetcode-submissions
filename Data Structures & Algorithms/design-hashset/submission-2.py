class MyHashSet:

    def __init__(self):
        self.arr = [None] * 10000

    def add(self, key: int) -> None:
        retrieved_list_index = key % len(self.arr)
        retrieved_list = self.arr[retrieved_list_index]

        if not retrieved_list:
            self.arr[retrieved_list_index] = ListNode(key)
            return
        
        prev = None
        curr = retrieved_list
        while curr:
            if curr.val == key:
                return 
            prev = curr
            curr = curr.next
        
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        retrieved_list_index = key % len(self.arr)
        retrieved_list = self.arr[retrieved_list_index]
        
        dummy = ListNode(-1, retrieved_list)
        prev = dummy
        curr = retrieved_list
        while curr:
            if curr.val == key:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        
        
        self.arr[retrieved_list_index] = dummy.next


    def contains(self, key: int) -> bool:
        retrieved_list_index = key % len(self.arr)
        retrieved_list = self.arr[retrieved_list_index]
        
        curr = retrieved_list
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False

class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

