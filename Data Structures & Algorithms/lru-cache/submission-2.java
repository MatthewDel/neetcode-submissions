class LRUCache {
    HashMap<Integer, Node> map = new HashMap<>();
    Node head;
    Node tail;
    int capacity;
    int running_capacity = 0;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {
        Node toReturn = this.map.get(key);
        if (toReturn == null) {
            return -1; 
        }

        // Case one: Head and not Tail
        if (this.head == toReturn && this.tail != toReturn) {
            Node toReturn_next = toReturn.next;
            toReturn_next.prev = null;

            toReturn.next = null;
            toReturn.prev = this.tail;
            this.tail.next = toReturn;
            
            this.head = toReturn_next;
            this.tail = toReturn;
        } else if (toReturn != this.head && toReturn != this.tail) {
            Node toReturn_prev = toReturn.prev;
            Node toReturn_next = toReturn.next;

            toReturn_prev.next = toReturn_next;
            toReturn_next.prev = toReturn_prev;

            this.tail.next = toReturn;
            toReturn.prev = this.tail;
            toReturn.next = null;

            this.tail = toReturn;
        }

        return toReturn.value;
    }
    
    public void put(int key, int value) {
        if (get(key) != -1) {
            this.map.get(key).value = value;
            return;
        }

        this.running_capacity++;

        if (head == null) {
            Node newNode = new Node(null, null, value, key);
            this.map.put(key, newNode);
            this.head = newNode;
            this.tail = newNode;
        } else {
            Node newNode = new Node(tail, null, value, key);
            this.map.put(key, newNode);
            this.tail.next = newNode;
            this.tail = newNode;
        }

        if (this.running_capacity > this.capacity) {
            Node head_next = head.next;
            this.map.remove(head.key);
            head.next = null;
            head_next.prev = null;

            if (head == tail) {
                head = head_next;
                tail = head_next;
            } else {
                head = head_next;
            }
            
            this.running_capacity--;
        }
    }
}


public class Node {
    public Node prev;
    public Node next;
    public int value;
    public int key;

    public Node(Node prev, Node next, int value, int key) {
        this.prev = prev;
        this.next = next;
        this.value = value;
        this.key = key;
    }
}
