class MyHashSet:

    def __init__(self):
        self.arr = [ListNode(-1)] * 10000

    def add(self, key: int) -> None:
        curr = self.arr[key % len(self.arr)]
        while curr.next:
            if curr.next.val == key:
                return 
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.arr[key % len(self.arr)]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.arr[key % len(self.arr)]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False
        
class ListNode:

    def __init__(self, val, next = None):
        self.val = val 
        self.next = next

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)