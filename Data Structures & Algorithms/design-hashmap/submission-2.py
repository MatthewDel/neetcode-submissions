class MyHashMap:

    def __init__(self):
        self.arr = [None] * 10000

    def put(self, key: int, value: int) -> None:
        retrieved_list_index = key % len(self.arr)
        retrieved_list = self.arr[retrieved_list_index]

        if not retrieved_list:
            self.arr[retrieved_list_index] = ListNode(value, key)
            return
        
        prev = None
        curr = retrieved_list
        while curr:
            if curr.key == key:
                curr.val = value
                return 
            prev = curr
            curr = curr.next
        
        prev.next = ListNode(value, key)

    def get(self, key: int) -> int:
        retrieved_list_index = key % len(self.arr)
        retrieved_list = self.arr[retrieved_list_index]
        
        curr = retrieved_list
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        retrieved_list_index = key % len(self.arr)
        retrieved_list = self.arr[retrieved_list_index]
        
        dummy = ListNode(-1, -1, retrieved_list)
        prev = dummy
        curr = retrieved_list
        while curr:
            if curr.key == key:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        
        
        self.arr[retrieved_list_index] = dummy.next

class ListNode:

    def __init__(self, val, key, next = None):
        self.val = val
        self.key = key
        self.next = next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)