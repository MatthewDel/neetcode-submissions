class PrefixTree {
    Node initialNode;

    public PrefixTree() {
         this.initialNode = new Node();
    }

    public void insert(String word) {
        Node dummy = this.initialNode;
        for(int i = 0; i < word.length(); i++) {
            int index = 'z' - word.charAt(i);
            if (dummy.map[index] == null) {
                Node newNode = new Node();
                dummy.map[index] = newNode;
            }
 
            dummy = dummy.map[index];
        }
        dummy.endOfWord = true;
    }

    public boolean search(String word) {
        Node dummy = this.initialNode;
        for(int i = 0; i < word.length(); i++) {
            int index = 'z' - word.charAt(i);
            if (dummy.map[index] == null) {
                return false;
            }
 
            dummy = dummy.map[index];
        }

        return dummy.endOfWord;
    }

    public boolean startsWith(String prefix) {
        Node dummy = this.initialNode;
        for(int i = 0; i < prefix.length(); i++) {
            int index = 'z' - prefix.charAt(i);
            if (dummy.map[index] == null) {
                return false;
            }
 
            dummy = dummy.map[index];
        }

        return true;
    }

    class Node {
        Node[] map;
        boolean endOfWord;

        public Node(){
            this.map = new Node[26];
        }
    }
}
